# Use official Python slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ../ml/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy ML code and model
COPY ../ml/ /app/ml/

# Copy FastAPI app code
COPY main.py /app/

# Copy the pre-trained model
COPY ../ml/model.pkl /app/ml/model.pkl

# Expose port FastAPI listens on
EXPOSE 8000

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
