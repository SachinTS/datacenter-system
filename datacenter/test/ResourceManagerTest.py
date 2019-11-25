class resourceManagerAlgorithmTests(unittest.TestCase):

    RAMLimit = 64
    CPULimit = 18


    # no active servers, no feasible servers, no idle servers
    caseOneServers = {

    }

    # no active servers, no feasible servers, idle servers
    caseTwoServers = {
        0:{"RAM":0,    "Cores":0, "Status":0},
        1:{"RAM":0,    "Cores":0, "Status":0},
        2:{"RAM":0,    "Cores":0,  "Status":0},
        3:{"RAM":0,    "Cores":0,  "Status":0}
    }

    # active servers, no feasible servers, idle servers
    caseThreeServers = {
        0:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        1:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        2:{"RAM":RAMLimit,    "Cores":CPULimit,  "Status":1},
        3:{"RAM":RAMLimit,    "Cores":CPULimit,  "Status":1}
    }

    # active servers, no feasible servers, idle servers
    caseFourServers = {
        0:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        1:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        2:{"RAM":0,    "Cores":0,  "Status":0},
        3:{"RAM":0,    "Cores":0,  "Status":0}
    }

    # active servers, feasible servers, no idle servers
    caseFiveServers = {
        0:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        1:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        2:{"RAM":RAMLimit,    "Cores":CPULimit,  "Status":1},
        3:{"RAM":16,    "Cores":6,  "Status":1},
        4:{"RAM":4,    "Cores":1,  "Status":1}
    }

    # active servers,  feasible servers, idle servers
    caseSixServers = {
        0:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        1:{"RAM":RAMLimit,    "Cores":CPULimit, "Status":1},
        2:{"RAM":16,    "Cores":6,  "Status":1},
        3:{"RAM":4,    "Cores":1,  "Status":1},
        4:{"RAM":0,    "Cores":0,  "Status":0},
        5:{"RAM":0,    "Cores":0,  "Status":0}
    }

    def testCaseOne(self):
        self.assertEqual(findOptimalServer("A", self.caseOneServers), None)

    def testCaseTwo(self):
        self.assertIn(findOptimalServer("A", self.caseTwoServers), [s for s in self.caseTwoServers if self.caseTwoServers[s]["Status"] == 0])

    def testCaseThree(self):
        self.assertEqual(findOptimalServer("A", self.caseThreeServers), None)

    def testCaseFour(self):
        self.assertIn(findOptimalServer("A", self.caseFourServers), [2,3])

    def testCaseFive(self):
        self.assertEqual(findOptimalServer("A", self.caseFiveServers), 3)

    def testCaseSix(self):
        self.assertEqual(findOptimalServer("A", self.caseSixServers), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
