# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Copy the current directory contents into the container at /app
COPY ./app /usr/src/app

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
