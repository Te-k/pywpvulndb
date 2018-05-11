import unittest
from pywpvulndb import PluginVersion

class TestPluginVersion(unittest.TestCase):
    def test_bigger(self):
        self.assertTrue(PluginVersion("1.2.4") > PluginVersion("0.1"))
        self.assertTrue(PluginVersion("1.2.4") > PluginVersion("0.1.1"))
        self.assertTrue(PluginVersion("1.2.4") > PluginVersion("1.1"))
        self.assertTrue(PluginVersion("1.2.4") > PluginVersion("1.1.2"))
        self.assertTrue(PluginVersion("1.2.4") > PluginVersion("1.2.3.2"))

    def test_smaller(self):
        self.assertTrue(PluginVersion("1.2.4") < PluginVersion("3"))
        self.assertTrue(PluginVersion("1.2.4") < PluginVersion("3.1"))
        self.assertTrue(PluginVersion("1.2.4") < PluginVersion("1.2.5"))
        self.assertTrue(PluginVersion("1.2.4") < PluginVersion("1.3"))
        self.assertTrue(PluginVersion("1.2.4") < PluginVersion("1.2.4.1"))

    def test_equal(self):
        self.assertEqual(PluginVersion("1.2.4"), PluginVersion("v1.2.4"))

if __name__ == '__main__':
    unittest.main()
