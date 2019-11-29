from  lib.resourceManager import ResourceManager
import unittest


class resourceManagerAlgorithmTests(unittest.TestCase):

    def testCaseOne(self):
        self.rm = ResourceManager()
        self.assertIsNotNone(self.rm.optimal_server("D"))



if __name__ == "__main__":
    unittest.main(verbosity=2)
