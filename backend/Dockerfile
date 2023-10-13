# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev

COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt


# Set the working directory in the container
WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Copy the current directory contents into the container at /app


# Run app.py when the container launches
CMD ["python","/app/main.py"]
