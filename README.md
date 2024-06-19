Here is the complete `README.md` with the port changed to 5000:


# Webhook Repository

This repository is designed to receive and display events from another repository via a webhook. It uses Flask and MongoDB.

## Requirements

- Python 3.9
- Flask
- MongoDB

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sanket3266/webhook-repo.git
    cd webhook-repo
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python run.py
    ```

## Docker Instructions

To containerize and run this project using Docker, follow these steps:

**Build the Docker image and run**:

    ```sh
    docker-compose up --build
    ```

### Dockerfile

Here is the `Dockerfile` used for this project:

```dockerfile
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
```


## Usage

This application listens for webhook events and displays them.

1. Set up a webhook in the source repository to point to this application's endpoint.
2. Start the application and monitor the incoming webhook events.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
