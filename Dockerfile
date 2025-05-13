FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/
COPY music/ ./music/

# Command to run the application
CMD ["python", "./src/main.py"]