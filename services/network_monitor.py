# services/network_monitor.py

import psutil
import logging
import time

logger = logging.getLogger(__name__)

class NetworkMonitor:
    def __init__(self, interval=60):
        """
        Initialize the NetworkMonitor with a specified interval.
        
        :param interval: Time interval in seconds for monitoring.
        """
        self.interval = interval

    def get_network_stats(self):
        """
        Retrieve current network statistics.
        
        :return: A dictionary containing network statistics.
        """
        logger.info("Gathering network statistics...")
        stats = psutil.net_if_stats()
        return {interface: {'is_up': interface_stats.isup, 'speed': interface_stats.speed}
                for interface, interface_stats in stats.items()}

    def monitor_network(self):
        """
        Continuously monitor network performance at the specified interval.
        """
        logger.info("Starting network monitoring...")
        while True:
            stats = self.get_network_stats()
            logger.info(f"Network Stats: {stats}")
            time.sleep(self.interval)

# Example usage
# network_monitor = NetworkMonitor(interval=60)
# network_monitor.monitor_network()
