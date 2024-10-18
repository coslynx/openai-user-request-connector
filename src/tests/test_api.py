import pytest
from fastapi.testclient import TestClient
from src.api.main import app
from unittest.mock import patch
from openai.error import RateLimitError, APIError, AuthenticationError, InvalidRequestError

# --- Fixtures ---

@pytest.fixture
def client():
    """Provides a TestClient instance for testing the API."""
    yield TestClient(app)

# --- Tests ---

class TestAPI:

    @patch("openai.OpenAI.completions.create")
    def test_generate_ai_response_success(self, mock_create, client):
        """Tests a successful AI response generation."""
        mock_create.return_value = {"choices": [{"text": "This is a test response."}]}
        response = client.post(
            "/api/v1/request",
            json={"text": "This is a test request.", "model": "text-davinci-003"},
        )
        assert response.status_code == 200
        assert response.json() == {
            "message": "Success",
            "response": "This is a test response.",
        }

    @patch("openai.OpenAI.completions.create", side_effect=RateLimitError())
    def test_generate_ai_response_rate_limit(self, mock_create, client):
        """Tests handling of OpenAI rate limiting errors."""
        response = client.post(
            "/api/v1/request",
            json={"text": "This is a test request.", "model": "text-davinci-003"},
        )
        assert response.status_code == 429
        assert response.json() == {"message": "Rate limit exceeded. Please try again later."}

    @patch("openai.OpenAI.completions.create", side_effect=APIError())
    def test_generate_ai_response_api_error(self, mock_create, client):
        """Tests handling of OpenAI API errors."""
        response = client.post(
            "/api/v1/request",
            json={"text": "This is a test request.", "model": "text-davinci-003"},
        )
        assert response.status_code == 500
        assert response.json() == {"message": "Error communicating with OpenAI API."}

    @patch("openai.OpenAI.completions.create", side_effect=AuthenticationError())
    def test_generate_ai_response_authentication_error(self, mock_create, client):
        """Tests handling of OpenAI authentication errors."""
        response = client.post(
            "/api/v1/request",
            json={"text": "This is a test request.", "model": "text-davinci-003"},
        )
        assert response.status_code == 401
        assert response.json() == {"message": "Invalid API key."}

    @patch("openai.OpenAI.completions.create", side_effect=InvalidRequestError())
    def test_generate_ai_response_invalid_request_error(self, mock_create, client):
        """Tests handling of OpenAI invalid request errors."""
        response = client.post(
            "/api/v1/request",
            json={"text": "This is a test request.", "model": "text-davinci-003"},
        )
        assert response.status_code == 400
        assert response.json() == {"message": "Invalid request parameters."}

    @patch("openai.OpenAI.completions.create", side_effect=Exception())
    def test_generate_ai_response_unexpected_error(self, mock_create, client):
        """Tests handling of unexpected errors."""
        response = client.post(
            "/api/v1/request",
            json={"text": "This is a test request.", "model": "text-davinci-003"},
        )
        assert response.status_code == 500
        assert response.json() == {"message": "Internal server error."}

    def test_validate_text_empty(self, client):
        """Tests validation of empty text input."""
        response = client.post("/api/v1/request", json={"text": ""})
        assert response.status_code == 400
        assert response.json() == {"detail": [{"loc": ["body", "text"], "msg": "Text cannot be empty", "type": "value_error"}]}