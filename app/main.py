from fastapi import FastAPI, HTTPException
from .weather_client import weather_client
from .cache import cache_service

app = FastAPI(title="Weather API")

@app.get("/weather/{location}")
async def get_weather(location: str):
    cache_key = f"weather:{location.lower()}"
    
    # 1. Try to get data from Redis cache
    cached_data = cache_service.get(cache_key)
    if cached_data:
        return {"source": "cache", "data": cached_data}

    # 2. If not in cache, fetch from Visual Crossing
    weather_data = await weather_client.get_weather(location)
    
    # 3. Store the result in Redis for future requests
    cache_service.set(cache_key, weather_data)
    
    return {"source": "api", "data": weather_data}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
