FROM python:3.11.3-alpine3.18
LABEL mantainer="danielalvestrab@gmail.com"

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python outputs to console immediately
ENV PYTHONUNBUFFERED 1

# Copy app code and scripts to the container
COPY djangoapp /djangoapp
COPY scripts /scripts
COPY entrypoint.sh /entrypoint.sh

# Working directory for the application
WORKDIR /djangoapp

# Exposing the Django default port
EXPOSE 8000

# Setup and install dependencies
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web && \
    chmod -R 775 /data/web/static && \
    chmod -R 775 /data/web/media && \
    chmod -R +x /scripts && \
    chmod +x /entrypoint.sh

# Add /scripts and /venv/bin to PATH
ENV PATH="/scripts:/venv/bin:$PATH"

# Use non-root user
USER duser

# Entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
