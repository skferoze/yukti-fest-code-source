FROM python:3.11-slim

# Set environment variables
ENV NAME "Feroze's Pipeline"

# Create the working directory
RUN mkdir /app
WORKDIR /app 

# Copy the Python script into the container image
# This assumes hello.py is in the same folder as the Dockerfile
COPY hello.py /app/

# Define the command to run the application (runs the script we copied)
CMD ["python", "hello.py"]