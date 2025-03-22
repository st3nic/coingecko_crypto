import logging
import requests
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/"
COINGECKO_NFT_API_URL = "https://api.coingecko.com/api/v3/nfts/"

class CoinGeckoSensor(Entity):
    """Representation of a CoinGecko sensor."""

    def __init__(self, config):
        self._api_key = config["api_key"]
        self._coin = config["coin"]
        self._currency = config["currency"]
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
        return f"{self._coin.capitalize()} Price in {self._currency.upper()}"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._currency.upper()

    @property
    def extra_state_attributes(self):
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
        try:
            response = requests.get(f"{COINGECKO_API_URL}{self._coin}")
            response.raise_for_status()
            data = response.json()
            self._state = f"{data['market_data']['current_price'][self._currency]:.2f}"
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

class NFTSensor(Entity):
    """Representation of an NFT sensor using CoinGecko NFT data."""
    def __init__(self, config):
        self._api_key = config["api_key"]
        self._nft_id = config["nft_id"]
        self._state = None
        self._floor_price = None
        self._volume_24h = None

    @property
    def name(self):
        return f"{self._nft_id.capitalize()} (Native Currency)"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {
            "floor_price": self._floor_price,
            "volume_24h": self._volume_24h,
        }

    def update(self):
        try:
            response = requests.get(f"{COINGECKO_NFT_API_URL}{self._nft_id}")
            response.raise_for_status()
            data = response.json()

            #Coin gecko nft api, data structure changes between NFT's. Handle this.
            self._state = f"{data['floor_price']['native_currency']:.2f}"
            self._floor_price = data['floor_price']['native_currency']
            self._volume_24h = data['volume_24h']['native_currency']

        except Exception as e:
            _LOGGER.error(f"Error fetching CoinGecko NFT data: {e}")

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up CoinGecko and NFT sensors."""
    if entry.data["type"] == "crypto":
        async_add_entities([CoinGeckoSensor(entry.data)], True)
    elif entry.data["type"] == "nft":
        async_add_entities([NFTSensor(entry.data)], True)