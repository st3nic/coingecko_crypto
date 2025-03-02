Home Assistant Integration for HACS to use the Public CoinGecko API

Firstly you will need to signup for a demo api account(This is free and no credit card info is required to sign up)

https://www.coingecko.com/en/api/pricing

Once signed up and you have generated and API Key you will need to select the coin id you want to track, use the developer test page to find the ID easily using your API key

https://docs.coingecko.com/reference/coins-list

Once you have the Coin ID you can add this repo as a custom repo in Hacs, after the repo has been added you install as a custom integration and follow the setup task.

You will need 3 things to add a coin to track

1. API Key
2. Coin ID
3. Select the currency you want to show, the options are currently "usd", "eur", "gbp", "cad", "aud", "jpy", "btc", "eth"

![alt text](<add sensor.png>)

Once selected you can save and the sensor will be available in Homeassistant.

Attributes currently supported are 24H High,24H Low,percentage change 7d,percentage change 14d,percentage change 30d,percentage change 60d,percentage change 200d,percentage change 1y

![alt text](image.png)


