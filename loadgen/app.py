import requests
import os
import time
from datetime import datetime
import sys


def loadgen():
    front_end = os.environ.get('F_HOST', "localhost")
    front_end_port = os.environ.get('F_PORT', "5000")
    sleep_time = os.environ.get('SLEEP_TIME', "5000")
    print("F_HOST: " + front_end)
    print("F_PORT: " + front_end_port)
    print("SLEEP_TIME: " + sleep_time)
    
    while (True):
        timeString = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        try:
            res = requests.get('http://' + front_end + ':' + front_end_port, timeout=.5)
            print(timeString + " - [loadgen] - Status: " + str(res.status_code) + " - " + res.text )
        except Exception as e:
            print(timeString + " - [loadgen] - Status: " + repr(e))
        time.sleep( int(sleep_time) / 1000 )

if __name__ == '__main__':
    sys.exit(loadgen())  