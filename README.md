# Check Status of Bockware Pool Miners
If you have ASIC miners hosted by Blockware Solutions and are using their Blockware Mining Pool. This program will check the status of your miners/workers and send push notification if their hashrate or efficiency drops below a certain harded coded threshold. Blockware uses Luxor for the API integration, which happens to have a [python client API](https://github.com/LuxorLabs/graphql-python-client). I am using [PushBullet](https://www.pushbullet.com/) for push notifications.


## Configuration
- You will need to generate a Luxor API key through the blockware mining account interface.
- You will need to register an account with PushBullet and generate an API key. 
- You will need to set two environmental variables for each of these APIs, namely: LUX_API and PUSH_API.  You can place the following in your .bashrc file and source it. 
    - ```export LUX_API="SOMEAPIKEY" PUSH_API="SOMEOTHERAPIKEY"```
- You will need to adjust the following global variables to fit your configuration. 
    - EFFICIENCY_BASELINE -> Blockware measures efficiency as a percentage. 
    - HASH_BASELINE -> This is a count of Hashes per second. 1TH = 1 * 10^12 or 1,000,000,000,000
    - *NUM_WORKERS -> The number of miners you have. 

*This configuration only takes into account a single subaccount with N number of workers, but the program can be easilty updated for other configurations. 
