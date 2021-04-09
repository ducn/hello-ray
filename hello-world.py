import os
import sys
import time
import ray
from ray import serve

HEAD_SERVICE_IP_ENV = "EXAMPLE_CLUSTER_RAY_HEAD_SERVICE_HOST"
HEAD_SERVICE_CLIENT_PORT_ENV = "EXAMPLE_CLUSTER_RAY_HEAD_SERVICE_PORT_CLIENT"

# Connect to the running Ray cluster.
head_service_ip = os.environ[HEAD_SERVICE_IP_ENV]
client_port = os.environ[HEAD_SERVICE_CLIENT_PORT_ENV]
ray.util.connect(f"{head_service_ip}:{client_port}")
# Connect to the running Ray cluster.
# ray.init(address="auto", _redis_password='5241590000000000')
# Bind on 0.0.0.0 to expose the HTTP server on external IPs.
serve.start(detached=True, http_options={"host": "0.0.0.0"})

def hello():
    return "hello world"

serve.create_backend("hello_backend", hello)
serve.create_endpoint("hello_endpoint", backend="hello_backend", route="/hello")
