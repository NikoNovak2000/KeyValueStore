# Base image to use
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install dependencies (uvicorn)
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn

# Expose the port
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]