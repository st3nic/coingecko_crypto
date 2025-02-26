# coingecko_crypto
Home Assistant Integration for HACS to use the Public CoinGecko API

Firstly you will need to signup for a demo api account(This is free and no credit card info is required to sign up)

https://www.coingecko.com/en/api/pricing

Once signed up and you have generated and API Key you will need to select the coin id you want to track, use the developer test page to find the ID easily using your API key

https://docs.coingecko.com/reference/coins-list

Once you have the Coin ID you can add this repo as a custom repo in Hacs, after the repo has been added you install as a custom integration and follow the setup task.

You will need 3 things to add a coin to track

1. API Key
2. Coin ID
3. Select the currency you want to show, the option are currenlty "usd", "eur", "gbp", "cad", "aud", "jpy", "btc", "eth"

Once selcted you can save and the sensor will be avaibale in Homeassistant.
