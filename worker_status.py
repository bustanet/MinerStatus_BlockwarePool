## IMPORTS ##
from luxor import API
import json
import os

## SETUP ##
API_KEY = os.getenv("LUX_API")
API = API(host = "https://api.beta.luxor.tech/graphql", method = 'POST', org = 'luxor', key = API_KEY)
USER = API.get_subaccounts(1)['data']['users']['edges'][0]['node']['username']
DEBUG = 0
EFFICIENCY_BASELINE = 98 # Measured as a percentage. ie 97% efficiency. 
HASH_BASELINE = 90000000000000 # Measured in hashes per second 1 TH = 1 X 10^12 hashes per second 
NUM_WORKERS = 6 # Number of workers in subaccount pool 

# Used for Debugging
SAMPLE_DATA = [{'node': {'workerName': '01x01', 'details1H': {'hashrate': '89000000000', 'status': 'Active', 'efficiency': '95.0000', 'validShares': '1475', 'staleShares': '0', 'badShares': '0', 'duplicateShares': '0', 'invalidShares': '0', 'lowDiffShares': '0'}}}]

## FUNCTIONS ##
def check_miner_efficiency():
    json_miner_data = get_miner_data()
    for miner in json_miner_data:
        name = miner['node']['workerName']
        efficiency = miner['node']['details1H']['efficiency']
        if float(efficiency) < EFFICIENCY_BASELINE:
            msg='[!] Efficiency Issue: Miner {}, efficiency below threshhold --> {}'.format(name,efficiency)
            return(msg)
        else:
            return(None)

def check_miner_hashrate():
    json_miner_data = get_miner_data()
    for miner in json_miner_data:
        name = miner['node']['workerName']
        hashrate = miner['node']['details1H']['hashrate']
        if float(hashrate) < HASH_BASELINE:
            msg='[!] Hashrate Issue: Miner {}, hashrate below threshold --> {}'.format(name,hashrate)
            return(msg)
        else:
            return(None)

def pretty_json(json_data):
    json_str = json.dumps(json_data, indent=2)
    print(json_str)

def get_miner_data(): 
    resp = API.get_worker_details_1H(USER, "BTC", NUM_WORKERS)

    if DEBUG == 1: 
        json_miner_data = SAMPLE_DATA
    else: 
        json_miner_data = resp['data']['miners']['edges']

    return(json_miner_data)


#check_miner_efficiency(json_miner_data)
#check_miner_hashrate(json_miner_data)
#pretty_json(json_miner_data)

