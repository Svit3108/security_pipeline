FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    ssh \
    wget \
    curl \
    python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy only necessary files into the container
COPY . /app/

# Adjust permissions more selectively if needed
RUN chmod 755 /app/

# Specify the default command to run when the container starts
CMD ["python3", "/app/"]
EXPOSE 3000
