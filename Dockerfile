# Use an official Python runtime as a parent image, as close as possible to your development environment.
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# If you have some packages that were installed with conda and they are not available via pip,
# you might need to find pip-equivalent packages or adjust your application dependencies accordingly.
RUN pip install --no-cache-dir -r requirements.txt

# Make sure to copy the .env file into your Docker image if the application requires it at build time.
# For security reasons, it's better to use it at runtime, not build time, as described later.
# COPY .env /app/.env  # Uncomment this line if absolutely necessary, but it's not recommended for sensitive data.

# The command to run the application
CMD ["python", "-m", "agents.tool_maker.unit_manager"]

# Expose any ports your application might need
EXPOSE 8081 
