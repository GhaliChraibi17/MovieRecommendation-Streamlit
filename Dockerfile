# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Clone the repo directly from GitHub
RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/GhaliChraibi17/MovieRecommendation-Streamlit.git /app

# Install the required Python packages
RUN export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to allow external access to the Streamlit app
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
