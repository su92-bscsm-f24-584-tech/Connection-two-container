from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    count = r.incr("hits")
    return f"Hello! This page has been visited {count} times."

@app.route('/set', methods=['POST'])
def set_value():
    key = request.json.get("key")
    value = request.json.get("value")
    if not key or not value:
        return jsonify({"error": "Provide key and value"}), 400
    r.set(key, value)
    return jsonify({"key": key, "value": value})

@app.route('/get/<key>')
def get_value(key):
    value = r.get(key)
    if value:
        return jsonify({"key": key, "value": value})
    else:
        return jsonify({"error": "Key not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
