import pandas as pd
from datetime import datetime

log_file = 'traffic_log.csv'

def log_packet(packet_info):
    packet_info['timestamp'] = datetime.now().isoformat()
    df = pd.DataFrame([packet_info])
    df.to_csv(log_file, mode='a', header=not file_exists(), index=False)

def file_exists():
    try:
        with open(log_file, 'r'):
            return True
    except FileNotFoundError:
        return False
