## IMPORTS ##
from luxor import API
import json
import os
import logging
import sys

## SETUP ##
API_KEY = os.getenv("LUX_API")
API = API(host = "https://api.beta.luxor.tech/graphql", method = 'POST', org = 'luxor', key = API_KEY)
USER = API.get_subaccounts(1)['data']['users']['edges'][0]['node']['username']
EFFICIENCY_BASELINE = 98 # Measured as a percentage. ie 97% efficiency. 
HASH_BASELINE = 90000000000000 # Measured in hashes per second 1 TH = 1 X 10^12 hashes per second 
NUM_WORKERS = 6 # Number of workers in subaccount pool 


## FUNCTIONS ##
def check_miner_efficiency(miner_dataset):
    msg = ''
    for miner in miner_dataset:
        name = miner['node']['workerName']
        efficiency = miner['node']['details1H']['efficiency']

        if efficiency == None:
            tmp_msg = '{}: did not report efficiency data. Offline?\n'.format(name)
            logging.error(tmp_msg)
            msg += tmp_msg

        elif float(efficiency) < EFFICIENCY_BASELINE:
            tmp_msg = '{}: efficiency of {} is below threshhold of {}.\n'.format(name,efficiency,EFFICIENCY_BASELINE)
            logging.error(tmp_msg)
            msg += tmp_msg

    return(msg)

def check_miner_hashrate(miner_dataset):
    msg = ''
    for miner in miner_dataset:
        name = miner['node']['workerName']
        hashrate = miner['node']['details1H']['hashrate']

        if hashrate == None:
            tmp_msg = "{}: did not report hashrate data. Offline?\n".format(name)
            logging.error(tmp_msg)
            msg += tmp_msg

        elif float(hashrate) < HASH_BASELINE:
            tmp_msg = '{}: hashrate of {} is below threshhold of {}.\n'.format(name,hashrate,HASH_BASELINE)
            logging.error(tmp_msg)
            msg += tmp_msg
  
    return(msg)

def check_offline(miner_dataset):
    msg = ''
    for miner in miner_dataset:
        name = miner['node']['workerName']
        status = miner['node']['details1H']['status']

        if status == 'Dead':
            tmp_msg = '{} is offline.\n'.format(name)
            logging.error(tmp_msg)
            msg += tmp_msg
    return(msg)

def get_miner_data(): 
    try:
        resp = API.get_worker_details_1H(USER, "BTC", NUM_WORKERS)
    except Exception as ex:
        logging.exception("Error trying to call luxor API with get_miner_data")
        sys.exit()

    json_miner_data = resp['data']['miners']['edges']
    logging.debug(json_miner_data)

    return(json_miner_data)
