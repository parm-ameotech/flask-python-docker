class SqlAlchemyHelper():
    def __init__(self, *args, **kwargs):
        self.connection = kwargs.get('connection')
        super().__init__(*args, **kwargs)
    
    def authenticate_user(self, username, password):
        return None
