import worker_status
import push_notification
from datetime import datetime
import logging
import sys
import os

# Logging 
HOME_PATH = os.path.dirname(__file__)
logging.basicConfig(filename=HOME_PATH + "/miner.log", filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Script Executed from {}'.format(HOME_PATH))

# Debugging
DEBUG = 0
SAMPLE_DATA = [{'node': {'workerName': '01x1', 'details1H': {'hashrate': '0', 'status': 'Active', 'efficiency': '0', 'validShares': '1114', 'staleShares': '0', 'badShares': '0', 'duplicateShares': '0', 'invalidShares': '8', 'lowDiffShares': '0'}}}, {'node': {'workerName': '01x02', 'details1H': {'hashrate': '95059532864261.6889', 'status': 'Active', 'efficiency': '0', 'validShares': '1564', 'staleShares': '0', 'badShares': '0', 'duplicateShares': '0', 'invalidShares': '0', 'lowDiffShares': '0'}}}, {'node': {'workerName': '01x03', 'details1H': {'hashrate': None, 'status': 'Dead', 'efficiency': None, 'validShares': None, 'staleShares': None, 'badShares': None, 'duplicateShares': None, 'invalidShares': None, 'lowDiffShares': None}}}, {'node': {'workerName': '01x04', 'details1H': {'hashrate': '0', 'status': 'Active', 'efficiency': '99.9312', 'validShares': '1453', 'staleShares': '0', 'badShares': '0', 'duplicateShares': '0', 'invalidShares': '1', 'lowDiffShares': '0'}}}, {'node': {'workerName': '01x05', 'details1H': {'hashrate': '95417632920844.5156', 'status': 'Active', 'efficiency': '99.5716', 'validShares': '1162', 'staleShares': '0', 'badShares': '0', 'duplicateShares': '0', 'invalidShares': '5', 'lowDiffShares': '0'}}}]

# Select dataset to use
if DEBUG == 0:
    miner_data = worker_status.get_miner_data()
else:
    miner_data = SAMPLE_DATA

# Check on miner status
hash_status = worker_status.check_miner_efficiency(miner_data)
efficiency_status = worker_status.check_miner_hashrate(miner_data)
offline_status = worker_status.check_offline(miner_data)
msg = hash_status + '\n' + efficiency_status + '\n' + offline_status

# Notification
try: 
    f = open(HOME_PATH + "/flags.txt", "r")
except Exception as ex:
    logging.exception("Error opening flags file for reading")

line = f.readline()
notified = line.split('=')[1].strip()
f.close()

if len(msg) > 0 and notified == 'False':
    try: 
        pass
        push_notification.notify("Mining Alert", msg)
    except Exception as ex:
        logging.exception("Error sending push notification")

    try:
        f = open(HOME_PATH + '/flags.txt', 'w')
    except Exception as ex:
        logging.exception("Error opening flags file for writing")

    f.write('notified=True')
    f.close()

    
