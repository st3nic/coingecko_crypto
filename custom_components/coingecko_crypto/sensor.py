import logging
import requests
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up CoinGecko sensor."""
    api_key = entry.data["api_key"]
    coin = entry.data["coin"]
    currency = entry.data["currency"]
    async_add_entities([CoinGeckoSensor(api_key, coin, currency)], True)

class CoinGeckoSensor(Entity):
    """Representation of a CoinGecko sensor."""

    def __init__(self, api_key, coin, currency):
        """Initialize the sensor."""
        self._api_key = api_key
        self._coin = coin
        self._currency = currency
        self._state = None
        self._24hLow = None
        self._24hHigh = None
        self._price_change_percentage_24h = None
        self._price_change_percentage_7d = None
        self._price_change_percentage_14d = None
        self._price_change_percentage_30d = None
        self._price_change_percentage_60d = None
        self._price_change_percentage_200d = None
        self._price_change_percentage_1y = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._coin.capitalize()} Price in {self._currency.upper()}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the selected currency."""
        return self._currency.upper()

    @property
    def extra_state_attributes(self):
        """Return additional attributes."""
        return {
            "high_24h": self._24hHigh,
            "low_24h": self._24hLow,
            "price_change_percentage_7d" : self._price_change_percentage_7d,
            "price_change_percentage_14d" : self._price_change_percentage_14d,
            "price_change_percentage_30d" : self._price_change_percentage_30d,
            "price_change_percentage_60d" : self._price_change_percentage_60d,
            "price_change_percentage_200d" : self._price_change_percentage_200d,
            "price_change_percentage_1y" : self._price_change_percentage_1y
        }

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get(f"{COINGECKO_API_URL}{self._coin}")
            response.raise_for_status()
            data = response.json()
            self._state = data['market_data']['current_price'][self._currency]
            self._24hLow = data['market_data']['low_24h'][self._currency]
            self._24hHigh = data['market_data']['high_24h'][self._currency]
            self._price_change_percentage_7d = data['market_data']['price_change_percentage_7d']
            self._price_change_percentage_14d = data['market_data']['price_change_percentage_14d']
            self._price_change_percentage_30d = data['market_data']['price_change_percentage_30d']
            self._price_change_percentage_60d = data['market_data']['price_change_percentage_60d']
            self._price_change_percentage_200d = data['market_data']['price_change_percentage_200d']
            self._price_change_percentage_1y = data['market_data']['price_change_percentage_1y']
        except Exception as e:
            _LOGGER.error(f"Error fetching CoinGecko data: {e}")
