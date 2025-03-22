import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = "coingecko_crypto"

CURRENCIES = ["usd", "eur", "gbp", "cad", "aud", "jpy", "btc", "eth"]

class CoinGeckoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CoinGecko Crypto Prices."""

    async def async_step_user(self, user_input=None):
        """Handle user-initiated configuration."""
        _LOGGER.debug("async_step_user called")
        return self.async_show_menu(
            step_id="menu", menu_options=["crypto", "nft"]
        )

    async def async_step_menu(self, user_input=None):
        """Handle menu options."""
        if user_input == "crypto":
            return await self.async_step_crypto()
        elif user_input == "nft":
            return await self.async_step_nft()

    async def async_step_crypto(self, user_input=None):
        """Configure cryptocurrency sensor."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=f"{user_input['coin']} in {user_input['currency']}", data={"type": "crypto", **user_input})

        data_schema = vol.Schema(
            {
                vol.Required("api_key"): str,
                vol.Required("coin", default="bitcoin"): str,
                vol.Required("currency", default="usd"): vol.In(CURRENCIES),
            }
        )
        return self.async_show_form(step_id="crypto", data_schema=data_schema, errors=errors)

    async def async_step_nft(self, user_input=None):
        """Configure NFT sensor."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=f"{user_input['nft_id']}", data={"type": "nft", **user_input})

        data_schema = vol.Schema(
            {
                vol.Required("api_key"): str,
                vol.Required("nft_id"): str
            }
        )
        return self.async_show_form(step_id="nft", data_schema=data_schema, errors=errors)