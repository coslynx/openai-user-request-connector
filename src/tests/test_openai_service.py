import pytest
from unittest.mock import patch
from src.services.openai_service import openai_service
from openai.error import RateLimitError, APIError, AuthenticationError, InvalidRequestError
from src.config.settings import settings

# --- Test Fixtures ---

@pytest.fixture
def openai_client():
    """Provides a mocked OpenAI client for testing."""
    client = patch("openai.OpenAI").start()
    yield client
    client.stop()

# --- Tests ---

class TestOpenAIService:

    @patch("openai.OpenAI.completions.create")
    def test_generate_response_success(self, mock_create, openai_client):
        """Tests a successful AI response generation."""
        mock_create.return_value = {"choices": [{"text": "This is a test response."}]}
        response = openai_service.generate_response(model="text-davinci-003", text="This is a test request.")
        assert response["message"] == "Success"
        assert response["response"] == "This is a test response."

    @patch("openai.OpenAI.completions.create", side_effect=RateLimitError())
    def test_generate_response_rate_limit(self, mock_create, openai_client):
        """Tests handling of OpenAI rate limiting errors."""
        with pytest.raises(RateLimitError):
            openai_service.generate_response(model="text-davinci-003", text="This is a test request.")

    @patch("openai.OpenAI.completions.create", side_effect=APIError())
    def test_generate_response_api_error(self, mock_create, openai_client):
        """Tests handling of OpenAI API errors."""
        with pytest.raises(APIError):
            openai_service.generate_response(model="text-davinci-003", text="This is a test request.")

    @patch("openai.OpenAI.completions.create", side_effect=AuthenticationError())
    def test_generate_response_authentication_error(self, mock_create, openai_client):
        """Tests handling of OpenAI authentication errors."""
        with pytest.raises(AuthenticationError):
            openai_service.generate_response(model="text-davinci-003", text="This is a test request.")

    @patch("openai.OpenAI.completions.create", side_effect=InvalidRequestError())
    def test_generate_response_invalid_request_error(self, mock_create, openai_client):
        """Tests handling of OpenAI invalid request errors."""
        with pytest.raises(InvalidRequestError):
            openai_service.generate_response(model="text-davinci-003", text="This is a test request.")

    @patch("openai.OpenAI.completions.create", side_effect=Exception())
    def test_generate_response_unexpected_error(self, mock_create, openai_client):
        """Tests handling of unexpected errors."""
        with pytest.raises(Exception):
            openai_service.generate_response(model="text-davinci-003", text="This is a test request.")

    def test_generate_response_with_parameters(self, openai_client):
        """Tests the generate_response function with additional parameters."""
        mock_create = openai_client.return_value.completions.create
        mock_create.return_value = {"choices": [{"text": "This is a test response with parameters."}]}
        response = openai_service.generate_response(
            model="text-davinci-003", text="This is a test request.", max_tokens=500, temperature=0.5
        )
        mock_create.assert_called_once_with(
            model="text-davinci-003", prompt="This is a test request.", max_tokens=500, temperature=0.5
        )
        assert response["message"] == "Success"
        assert response["response"] == "This is a test response with parameters."