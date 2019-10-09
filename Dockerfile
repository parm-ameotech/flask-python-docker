# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory
WORKDIR /neuraldistribution


COPY . /neuraldistribution/

# # Copy the current directory contents into the container at /app
# ADD . /neural-distribution/
# Install any needed packages specified in requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# EXPOSE 8001
RUN chmod +x /neuraldistribution/docker-entrypoint.sh



