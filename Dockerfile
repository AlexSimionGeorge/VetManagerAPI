FROM python:3.12.9-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app will run on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
