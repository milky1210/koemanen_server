# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Update and install system packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev libsndfile1  # libsndfile1を追加

# Copy requirements.txt and install Python packages
COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# FastAPI and Uvicorn are already in requirements.txt, so you don't have to install them here again.
# But if you want to make sure they are installed, you can keep the following line.
# RUN pip install fastapi uvicorn

# Copy the current directory contents into the container at /app
# (This is a comment for now; you'll have to add this step when you're ready)

# Run app.py when the container launches
CMD ["python","/app/main.py"]
