"""
Gunicorn configuration file for Mavus Django application
"""

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"

# Process naming
proc_name = "mavus_gunicorn"

# Server mechanics
daemon = False
pidfile = "/var/run/gunicorn/gunicorn.pid"
user = None
group = None
tmp_upload_dir = None

# SSL (uncomment if using HTTPS directly with Gunicorn)
# keyfile = "/path/to/keyfile"
# certfile = "/path/to/certfile"
