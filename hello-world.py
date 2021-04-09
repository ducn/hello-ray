import ray
from ray import serve

# Connect to the running Ray cluster.
ray.init(address="auto")
# Bind on 0.0.0.0 to expose the HTTP server on external IPs.
serve.start(detached=True, http_options={"host": "0.0.0.0"})

def hello():
    return "hello world"

serve.create_backend("hello_backend", hello)
serve.create_endpoint("hello_endpoint", backend="hello_backend", route="/hello")
