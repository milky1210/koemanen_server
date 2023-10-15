# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libgl1-mesa-dev \
    libsndfile1 \
    ffmpeg

# Copy requirements and install Python packages
COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Run app.py when the container launches
CMD ["python","/app/main.py"]
