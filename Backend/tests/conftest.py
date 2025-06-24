import pytest
import os
from unittest.mock import MagicMock, patch

# Set environment variable before any imports
os.environ["MONGO_URL"] = "mongodb://localhost:27017/test_db"

@pytest.fixture
def mock_employees_collection():
    """Mock MongoDB collection for testing"""
    return MagicMock()

@pytest.fixture(autouse=True)
def mock_database():
    """Auto-use fixture to mock database connections"""
    with patch('database.MongoClient') as mock_client:
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection
        yield mock_collection