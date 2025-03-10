"""
fruityvice_client.py

Provides a simple, object-oriented client to interact with the FruityVice API.

Features:
- Fetch fruit data by name (e.g., "Banana", "Strawberry").
- Raises exceptions or returns None if the fruit is not recognized or if the service fails.
- Designed for easy extension with additional API calls (family, genus, etc.).

Usage Example (Library):
    >>> from fruityvice_client import FruityViceClient
    >>> client = FruityViceClient()
    >>> data = client.get_fruit_info("Banana")
    >>> print(data)
"""

import requests


class FruityViceClient:
    """
    A client for interacting with the FruityVice fruit lookup API.
    """

    def __init__(self, base_url="https://www.fruityvice.com/api/fruit"):
        """
        Initialize the FruityViceClient with an optional custom base URL.
        """
        self.base_url = base_url

    def get_fruit_info(self, fruit_name: str) -> dict or None:
        """
        Retrieves information about a fruit from the FruityVice API.

        :param fruit_name: The name of the fruit (e.g., 'Banana', 'Strawberry').
        :return: A dictionary with fruit data if successful, or None if unrecognized.
        :raises RuntimeError: If the API request fails or times out.
        :raises ValueError: If the API response cannot be parsed as valid JSON.
        """
        url = f"{self.base_url}/{fruit_name.lower()}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Unable to connect to FruityVice API: {e}")

        try:
            data = response.json()
        except ValueError:
            raise ValueError("Invalid JSON received from the FruityVice API.")

        # If the API doesn't return a valid fruit structure
        if not isinstance(data, dict) or "name" not in data:
            return None

        return data