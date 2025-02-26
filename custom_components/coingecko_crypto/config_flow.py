import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

DOMAIN = "coingecko_crypto"

CURRENCIES = ["usd", "eur", "gbp", "cad", "aud", "jpy", "btc", "eth"]

class CoinGeckoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CoinGecko Crypto Prices."""

    async def async_step_user(self, user_input=None):
        """Handle user-initiated configuration."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=f"{user_input['coin']} in {user_input['currency']}", data=user_input)

        data_schema = vol.Schema(
            {
                vol.Required("api_key"): str,
                vol.Required("coin", default="bitcoin"): str,
                vol.Required("currency", default="usd"): vol.In(CURRENCIES),
            }
        )
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
