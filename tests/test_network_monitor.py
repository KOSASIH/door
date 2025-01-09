# tests/test_network_monitor.py

import unittest
from services.network_monitor import NetworkMonitor

class TestNetworkMonitor(unittest.TestCase):
    def setUp(self):
        self.network_monitor = NetworkMonitor()

    def test_check_connection(self):
        status = self.network_monitor.check_connection()
        self.assertTrue(status, "Network connection should be active.")

    def test_get_network_stats(self):
        stats = self.network_monitor.get_network_stats()
        self.assertIn('latency', stats, "Network stats should include latency.")
        self.assertIn('bandwidth', stats, "Network stats should include bandwidth.")

if __name__ == '__main__':
    unittest.main()
