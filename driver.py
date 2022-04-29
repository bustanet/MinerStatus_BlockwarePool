import worker_status
import push_notification
from datetime import datetime
import logging
import sys
import os

logpath = os.path.dirname(__file__) + "/miner.log"
logging.basicConfig(filename=logpath, filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Script Executed')

error_msg = ""

try: 
    hash_status = worker_status.check_miner_efficiency()
    efficiency_status = worker_status.check_miner_hashrate()
except Exception as ex: 
    logging.exception("Error checking miner status.")
    sys.exit()
else: 
    if hash_status != None: 
        error_msg += (hash_status + "\n")

    if efficiency_status != None: 
        error_msg += (efficiency_status + "\n")

if len(error_msg) > 0:
    try: 
        push_notification.notify("Mining Alert", error_msg)
    except Exception as ex:
        logging.exception("Error sending push notification")
    else:
        logging.info("Miner performance is degraded.")
        logging.info(error_msg)        


