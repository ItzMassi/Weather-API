import httpx
from fastapi import HTTPException
from .config import settings

class WeatherClient:
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

    async def get_weather(self, location: str):
        params = {
            "unitGroup": "metric",
            "key": settings.visual_crossing_api_key,
            "contentType": "json"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.BASE_URL}/{location}", params=params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 400:
                    raise HTTPException(status_code=400, detail="Invalid location provided")
                raise HTTPException(status_code=502, detail="Error fetching data from weather provider")
            except Exception:
                raise HTTPException(status_code=500, detail="Internal server error")

weather_client = WeatherClient()
