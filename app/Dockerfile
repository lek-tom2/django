# Dockerfile

FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder

EXPOSE 8000
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

# Copy application source code
COPY . /app

# Stage 2: Development environment setup
FROM builder as dev-envs

# Install git, OpenSSH, bash, curl, and wget
RUN apk update && apk add --no-cache git openssh bash curl wget

# Create user 'docker' for non-root SSH access
RUN addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker docker

# Configure SSH for password authentication
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config && \
    echo "docker:docker" | chpasswd && \
    ssh-keygen -A


# Add Zed binary to PATH
RUN echo 'export PATH=$HOME/.local/bin:$PATH' >> /home/docker/.bashrc

# Expose SSH and Django server ports
EXPOSE 22 8000

# Start both sshd and Django server
CMD ["/bin/sh", "-c", "/usr/sbin/sshd && python3 manage.py runserver 0.0.0.0:8000"]
