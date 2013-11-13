import shopbothelper

import unittest

class TestShopBotHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_dust_collector_power_off(self):
        shopbothelper.spindle_current = 200
        shopbothelper.update_dustcollector_power()
        self.assertEqual(shopbothelper.dust_collector_power, False)

    def test_dust_collector_power_on(self):
        shopbothelper.spindle_current = 700
        shopbothelper.update_dustcollector_power()
        self.assertEqual(shopbothelper.dust_collector_power, True)

if __name__ == '__main__':
    unittest.main()
