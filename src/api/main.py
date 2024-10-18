from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, validator
from typing import Optional
from openai import OpenAI
import os
import logging

# --- Import Statements ---

# Core Modules:
import logging

# Third-Party:
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, validator
from typing import Optional
from openai import OpenAI
import os

# Internal:
from src.config.settings import settings
from src.services.openai_service import openai_service

# --- Environment Variables and Configuration ---

# Load environment variables using dotenv:
from dotenv import load_dotenv
load_dotenv()

# --- Logger Configuration ---

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
)

# --- Application Initialization ---

app = FastAPI()

# --- CORS Configuration ---

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "https://localhost:3000",
    "https://localhost:8000",
    "https://localhost:8080",
    "https://127.0.0.1:8080",
    "https://127.0.0.1:8000",
    "https://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---

class UserRequest(BaseModel):
    text: str
    model: str = "text-davinci-003"
    max_tokens: Optional[int] = 1024
    temperature: Optional[float] = 0.7

    @validator('text')
    def text_validation(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty")
        return value

# --- API Endpoints ---

@app.post("/api/v1/request")
async def generate_ai_response(request: Request, user_request: UserRequest):
    try:
        logging.info(f"Received user request: {user_request.json()}")

        # Handle potential rate limiting issues gracefully:
        response = await openai_service.generate_response(user_request.model, user_request.text, user_request.max_tokens, user_request.temperature)

        logging.info(f"Successful AI response: {response.choices[0].text}")

        # Format the AI response:
        response_data = {
            "message": "Success",
            "response": response.choices[0].text
        }

        return JSONResponse(content=jsonable_encoder(response_data))

    except openai.error.RateLimitError as e:
        logging.error(f"Rate Limit Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Rate limit exceeded. Please try again later."}), status_code=429)

    except openai.error.APIError as e:
        logging.error(f"OpenAI API Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Error communicating with OpenAI API."}), status_code=500)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error."}), status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")