# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory
WORKDIR /neural-distribution


COPY . /neural-distribution/

# # Copy the current directory contents into the container at /app
# ADD . /neural-distribution/
# Install any needed packages specified in requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# EXPOSE 8001
RUN chmod +x /neural-distribution/docker-entrypoint.sh



