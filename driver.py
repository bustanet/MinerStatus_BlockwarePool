import worker_status
import push_notification

error_msg = ""
hash_status = worker_status.check_miner_efficiency()
efficiency_status = worker_status.check_miner_hashrate()

if hash_status != None: 
    error_msg += hash_status

if efficiency_status != None: 
    error_msg += "\n" + efficiency_status

if len(error_msg) > 0:
    push_notification.notify("Mining Alert", error_msg)



