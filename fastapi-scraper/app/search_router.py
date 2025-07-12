from fastapi import APIRouter, Request
from app.scraper_runner import run_spiders

router = APIRouter()

@router.post("/api/search_hotels")
async def search_hotels(payload: dict):
    city = payload.get("city")
    results = await run_spiders(city)
    return results
