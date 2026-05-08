# Weather API with Redis Caching

A fast, containerized Python API that fetches weather data from Visual Crossing and caches results in Redis for improved performance.

## 🚀 How it Works

1.  **FastAPI**: A modern web framework for building APIs with Python. It handles incoming requests (like `GET /weather/London`).
2.  **Visual Crossing API**: A 3rd party service that provides accurate weather data.
3.  **Redis**: An in-memory data structure store used here as a cache.
    *   When you request weather for a city, the API first checks Redis.
    *   If the data is there (a "cache hit"), it returns it immediately.
    *   If not (a "cache miss"), it fetches it from Visual Crossing, saves it in Redis for 30 minutes, and then returns it.
4.  **Docker**: Packages the application and Redis so they run identically on any machine.

## 🛠️ Setup

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
- A Visual Crossing API Key ([Get one here](https://www.visualcrossing.com/weather-api)).

### 2. Configuration
Copy the `.env.example` file to a new file named `.env` and add your API key:
```bash
cp .env.example .env
```
Edit `.env`:
```env
VISUAL_CROSSING_API_KEY=your_actual_key_here
```

### 3. Run with Docker
Start the entire stack with one command:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## 📡 API Endpoints

- **Get Weather**: `GET /weather/{location}`
  - Example: `http://localhost:8000/weather/London`
- **Health Check**: `GET /health`

## 📂 Project Structure
- `app/main.py`: The entry point and API routes.
- `app/weather_client.py`: Logic for talking to the Visual Crossing API.
- `app/cache.py`: Logic for interacting with Redis.
- `app/config.py`: Configuration management using environment variables.
- `Dockerfile` & `docker-compose.yml`: Containerization and orchestration.
