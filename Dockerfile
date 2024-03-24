# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# No dependencies to install for this simple script, but if you had any, they would be installed here.
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# This line can be omitted for this particular application since it's a CLI app, but included for completeness.
EXPOSE 80

# Run motivational_quotes.py when the container launches
CMD ["python", "./app.py"]