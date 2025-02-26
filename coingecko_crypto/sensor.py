import logging
import requests
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up CoinGecko sensor."""
    api_key = entry.data["api_key"]
    coin = entry.data["coin"]
    async_add_entities([CoinGeckoSensor(api_key, coin)], True)

class CoinGeckoSensor(Entity):
    """Representation of a CoinGecko sensor."""

    def __init__(self, api_key, coin):
        """Initialize the sensor."""
        self._api_key = api_key
        self._coin = coin
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._coin.capitalize()} Price"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "USD"

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get(f"{COINGECKO_API_URL}?ids={self._coin}&vs_currencies=usd")
            response.raise_for_status()
            data = response.json()
            self._state = data.get(self._coin, {}).get("usd", "N/A")
        except Exception as e:
            _LOGGER.error(f"Error fetching CoinGecko data: {e}")
