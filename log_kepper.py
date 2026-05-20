# log_keeper.py - Attack Logger

import logging
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s | %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('attack_records.txt'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("NEUTRON")

def log_attack(target, result):
    logger.info(f"🔥 ATTACK | Target: {target} | Result: {result}")

print("📋 LOG KEEPER READY")