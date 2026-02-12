
# Multi-Container Flask + Redis App

A simple multi-container project using **Docker Compose**, demonstrating how a Flask web application can communicate with a Redis database.  

This project is ideal for learning **DevOps concepts**, **container networking**, and **data persistence**.

---

## **Project Structure**

```

docker_2/
├── app/
│   ├── app.py            # Flask application
│   ├── Dockerfile        # Dockerfile for Flask app
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # This file

````

---

## **What this project demonstrates**

- Running **multiple containers** together: Flask + Redis  
- Container **communication** using Docker network  
- Using **environment variables** to configure containers  
- Basic **CRUD operations** with Redis (in-memory key-value store)  
- Docker Compose orchestration

---

## **Prerequisites**

- Docker & Docker Compose installed  
- Linux / Windows / macOS terminal  

---

## **Getting Started**

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd docker_2
````

2. **Build and run containers**:

```bash
docker compose up --build
```

3. **Access the Flask app**:

Open your browser:

```
http://localhost:5000/
```

---

## **How to Use**

### Home Page (Visit Counter)

```bash
curl http://localhost:5000/
```

* Each visit increments a counter stored in Redis.

### Set a Key-Value Pair

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"key":"name","value":"Tobi"}' \
http://localhost:5000/set
```

### Get a Key

```bash
curl http://localhost:5000/get/name
```

---

## **Access Redis Directly**

```bash
docker exec -it docker_2_redis_1 redis-cli
```

Redis CLI commands:

```redis
KEYS *
GET name
INCR hits
```

---

## **Stopping the Containers**

```bash
docker compose down
```

---

## **Optional: Persistent Redis Data**

Add this to `docker-compose.yml` under `redis`:

```yaml
volumes:
  - redis_data:/data

volumes:
  redis_data:
```

* Data will now persist even if the Redis container is restarted.

---

## **Why This Project is Useful for DevOps**

* Teaches **containerization and orchestration**
* Shows **service communication and environment variables**
* Demonstrates **data persistence strategies**
* Provides a simple microservice-like environment

---
