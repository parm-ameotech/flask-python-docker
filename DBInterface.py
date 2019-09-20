import datetime
import numpy
import pandas as pd
import psycopg2
import psycopg2.extras
from influxdb import DataFrameClient

from config import PSQL_USER, PSQL_PASS, PSQL_HOST, PSQL_PORT, PSQL_DB


class DBManager:
    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if DBManager.__instance == None:
            DBManager()
        return DBManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DBManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DBManager.__instance = self
        self.psql_cursor = None
        self.psql_connection = None
        self.psql_user = PSQL_USER
        self.psql_pass = PSQL_PASS
        self.psql_host = PSQL_HOST
        self.psql_port = PSQL_PORT
        self.psql_db = PSQL_DB

        self.connect()

    def get_cursor(self):
        if not self.is_connected():
            self.connect()
        return self.psql_cursor

    def is_connected(self):
        if self.psql_connection is not None and self.psql_cursor is not None:
            return True
        else:
            return False

    # connect operation is a critical section only one thread can execute at a time
    def connect(self):
        if self.is_connected():
            print("PostgreSQL DB is already connected")
            return
        try:
            self.psql_connection = psycopg2.connect(
                                    user=self.psql_user,
                                    password=self.psql_pass,
                                    host=self.psql_host,
                                    port=self.psql_port,
                                    database=self.psql_db
                                )
            self.psql_connection.autocommit = True
            self.psql_cursor = self.psql_connection.cursor()
            print("Connected to PostgreSQL DB")
        except (Exception, psycopg2.Error) as error:
            print ("Error connecting to PostgreSQL DB", error)      

    def get_columns_names(self, df, datetime_index = True):
        if datetime_index:
            df_columns = ['DateTime']
            df_columns.extend(list(df))
            return df_columns
        else:
            return list(df)

    def get_columns_types(self, df, unique_datetime = True, datetime_index = True):
        types = []
        col_type = "CHAR(80)"
        if len(df) > 0:
            # handle datetime being an index
            if datetime_index:
                df = df.reset_index()
            for column in list(df.columns):
                if isinstance(df[column][0], datetime.datetime):
                    if unique_datetime and (column.lower() == "index" or column.lower() == "datetime"):
                        col_type = "TIMESTAMP without time zone UNIQUE"
                    else:
                        col_type = "TIMESTAMP without time zone"
                elif isinstance(df[column][0], (str)):
                    col_type = "CHAR(80)"
                elif isinstance(df[column][0], (int, numpy.int32, numpy.int64)):
                    col_type = "INT"
                elif isinstance(df[column][0], (float, numpy.float32, numpy.float64)):
                    col_type = "REAL"
                types.append(col_type)

        return types

    def create_table(self, table_name, columns, types, drop_if_exists = False):
        if not self.is_connected():
            self.connect()
        try:
            # create uuid extension if it doesn't exist
            self.psql_cursor.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
            
            # drop table if table already exists
            if drop_if_exists:
                drop_table_query = "DROP TABLE IF EXISTS {}".format(table_name)
                self.psql_cursor.execute(drop_table_query)
                
            create_table_query  = "CREATE TABLE IF NOT EXISTS {} (Index UUID PRIMARY KEY DEFAULT uuid_generate_v4 (),".format(table_name)
            for i in range(len(columns)):
                create_table_query  += "{} {}".format(columns[i], types[i])
                if (i != len(columns) - 1):
                    create_table_query  += ","
            create_table_query  += ");"
            
            self.psql_cursor.execute(create_table_query)
        except (Exception, psycopg2.Error) as error:
            print ("Error while creating table {}".format(table_name), error)
                
    def insert_into_table(self, table_name, df, erase_data, datetime_index = True):
        if not self.is_connected():
            self.connect()
        try:
            if erase_data:
                sql_delete_query = "Delete from {}".format(table_name)
                self.psql_cursor.execute(sql_delete_query)
                count = self.psql_cursor.rowcount
                print(count, "Record deleted successfully from {}".format(table_name))

            if len(df) > 0:
                df_columns = self.get_columns_names(df, datetime_index)

                # create a copy of the df
                dfdp = df.copy()
                if datetime_index:
                    dfdp = dfdp.reset_index()
                dfdp = dfdp.where(pd.notnull(dfdp), None)

                # create (col1,col2,...)
                columns = ",".join(df_columns)

                # create VALUES('%s', '%s",...) one '%s' per column
                values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))

                #create INSERT INTO table (columns) VALUES('%s',...)
                insert_stmt = "INSERT INTO {} ({}) {} ON CONFLICT DO NOTHING".format(table_name,columns,values)
                psycopg2.extras.execute_batch(self.psql_cursor, insert_stmt, dfdp.values)
                print("Inserted dataframe successfully to {}".format(table_name))
        except (Exception, psycopg2.Error) as error:
            print("Error while inserting to table {}".format(table_name), error)

    def get_table_content(self, table_name, where_columns=[], where_values=[], where_signs=[]):
        if not self.is_connected():
            self.connect()
            
        df = None
        where_query = ""
        for i in range(len(where_columns)):
            where_query += "{} {} {}".format(where_columns[i], where_signs[i], where_values[i])
            if i != (len(where_columns) - 1):
                where_query += " AND "

        if where_query != "":
            select_table  = "SELECT * FROM {} WHERE {};".format(table_name, where_query)
        else:
            select_table  = "SELECT * FROM {};".format(table_name)
        
        try:
            self.psql_cursor.execute(select_table)
            colnames = [desc[0] for desc in self.psql_cursor.description]
            df = pd.DataFrame(self.psql_cursor.fetchall(), columns=colnames)
        except (Exception, psycopg2.Error) as error :
            print ("Error while getting table content for table {}".format(table_name), error)
        return df

    def get_last_record_timestamp(self, table_name):
        if not self.is_connected():
            self.connect()
        last_timestamp = None
        select_table  = "SELECT datetime FROM {} ORDER BY datetime DESC LIMIT 1;".format(table_name)
        try:
            self.psql_cursor.execute(select_table)
            last_timestamp = self.psql_cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            print ("Error while getting last timestamp for table {}".format(table_name), error)

        if last_timestamp is not None and len(last_timestamp) == 1:
            return last_timestamp[0]
        else:
            return None

    def close_connection(self):
        if self.psql_cursor is not None:
            self.psql_cursor.close()
        if self.psql_connection is not None:
            self.psql_connection.close

