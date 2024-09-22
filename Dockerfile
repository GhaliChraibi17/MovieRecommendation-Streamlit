# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install git to allow cloning of the repository
RUN apt-get update && apt-get install -y git

# Clone the repo directly from GitHub
# Use a separate command to invalidate cache
RUN git clone https://github.com/GhaliChraibi17/MovieRecommendation-Streamlit /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to allow external access to the Streamlit app
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
