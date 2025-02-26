import logging
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

DOMAIN = "coingecko_crypto"
_LOGGER = logging.getLogger(__name__)

CONF_API_KEY = "api_key"
CONF_COIN = "coin"
CONF_CURRENCY = "currency"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_API_KEY): cv.string,
                vol.Required(CONF_COIN): cv.string,
                vol.Required(CONF_CURRENCY): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the CoinGecko integration."""
    if DOMAIN in config:
        hass.data[DOMAIN] = config[DOMAIN]
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up CoinGecko from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    
    return True
