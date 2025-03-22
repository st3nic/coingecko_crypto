Home Assistant Integration for HACS to use the Public CoinGecko API

** WARNING Breaking changes from V1 with adding suport for NFT's **

Firstly you will need to signup for a demo api account(This is free and no credit card info is required to sign up)

https://www.coingecko.com/en/api/pricing

Once signed up and you have generated an API Key you will need to select the coin or NFT id you want to track, use the developer test page to find the ID easily using your API key

https://docs.coingecko.com/reference/coins-list

You can also track NFT's listed at the below address

https://docs.coingecko.com/v3.0.1/reference/nfts-list

Add this repo to HACS then restart Home Assistant, Search for the integration in the available integrations and click add.

Select which type of entity you would like to add.

![alt text](<select type.png>)

If adding a coin you will then see the below image when you need to enter your API key, coin id and select which currency you would like to use.

![alt text](<add sensor.png>)

If adding an NFT you will see the below image where you need to add your API key and enter the NFT id.

![alt text](<add nft.png>)

Once selected you can save and the sensor will be avaibale in Homeassistant.

![alt text](image.png)


