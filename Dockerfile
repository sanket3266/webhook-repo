# Use the official Python 3.9 slim image from the Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file from the local machine to the container
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy all the files from the local machine's current directory to the container's /app directory
COPY . .

# Set environment variables for the Flask application
# FLASK_APP tells Flask the entry point of the application
ENV FLASK_APP=run.py
# FLASK_RUN_HOST sets the host to 0.0.0.0 to ensure the server is accessible from outside the container
ENV FLASK_RUN_HOST=0.0.0.0

# Specify the command to run the Flask application
CMD ["flask", "run"]
