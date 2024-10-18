from typing import Optional
import logging
from openai import OpenAI
from openai.error import RateLimitError, APIError, AuthenticationError, InvalidRequestError
from fastapi import HTTPException, status
from src.config.settings import settings

logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def generate_response(self, model: str, text: str, max_tokens: Optional[int] = 1024, temperature: Optional[float] = 0.7) -> dict:
        try:
            logger.info(f"Calling OpenAI API with model: {model}, text: {text}, max_tokens: {max_tokens}, temperature: {temperature}")
            response = await self.client.completions.create(
                model=model,
                prompt=text,
                max_tokens=max_tokens,
                temperature=temperature
            )
            logger.info(f"OpenAI API response: {response.choices[0].text}")
            return {"message": "Success", "response": response.choices[0].text}
        except RateLimitError as e:
            logger.error(f"Rate Limit Error: {e}")
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded. Please try again later.")
        except APIError as e:
            logger.error(f"OpenAI API Error: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error communicating with OpenAI API.")
        except AuthenticationError as e:
            logger.error(f"Authentication Error: {e}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key.")
        except InvalidRequestError as e:
            logger.error(f"Invalid Request Error: {e}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request parameters.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")

openai_service = OpenAIService()