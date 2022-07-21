# Importing and using python slim image version
FROM python:3.9.12-slim

# Using the default python image path
WORKDIR /usr/src/app

# Copy and install the flask requirements
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

# Exposes the default flask port
EXPOSE 5000

# Copy and execute the whole flask app
COPY . .
CMD ["python", "./src/dev/wsgi.py"]
