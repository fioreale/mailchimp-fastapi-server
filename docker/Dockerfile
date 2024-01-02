# Stage 1: Build stage - Install dependencies and create requirements.txt
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the working directory
COPY pyproject.toml poetry.lock* /app/

# Install dependencies in a way that they can be copied to the next stage
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# ────────────────────────────────────────────────────────────────────────── ✣ ─

# Stage 2: Run stage - Set up the runtime environment and run the application
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt from the builder stage
COPY --from=builder /app/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY src/ /app/src/
COPY .env /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
