# Use the official lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files and buffer outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy project files into the container
COPY . /app

# Run the interactive application when the container starts
CMD ["python", "main.py"]