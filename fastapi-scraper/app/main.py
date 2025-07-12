# app/main.py
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI server is working!"}

class SearchRequest(BaseModel):
    city: str = Field(..., description="City to search hotels in")
    min_price: Optional[float] = Field(None, description="Minimum price filter")
    max_price: Optional[float] = Field(None, description="Maximum price filter")
    rating: Optional[float] = Field(None, description="Minimum star rating filter (e.g. 4.0)")

@app.post("/api/search_hotels")
async def search_hotels(payload: SearchRequest):
    city = payload.city
    return {
        "city": city,
        "results": [
            {
                "name": "Hotel Grand Palace",
                "image": "https://via.placeholder.com/300x200?text=Hotel+1",
                "rating": "4.5",
                "booking_price": "$150",
                "agoda_price": "$140",
                "best_price": "$140",
                "best_source": "Agoda",
                "url": "https://agoda.com/hotel-grand-palace"
            },
            {
                "name": "City Center Inn",
                "image": "https://via.placeholder.com/300x200?text=Hotel+2",
                "rating": "4.0",
                "booking_price": "$120",
                "agoda_price": "$130",
                "best_price": "$120",
                "best_source": "Booking.com",
                "url": "https://booking.com/city-center-inn"
            }
        ]
    }
