
'''
class for declaring all the contants required by the app.
This helps in managing contants at one place.
'''

class AppConstants(object):
    LOGGING_CONFIG_FILE = "lib/logging_config.ini"
    LOG_FILE_NAME = "datacenter.log"
    CONTAINER = {
        "A":{"RAM":4,   "Cores":1},
        "B":{"RAM":4,   "Cores":2},
        "C":{"RAM":16,  "Cores":2},
        "D":{"RAM":32,  "Cores":3}
    }
    DB_FILE = "lib/dataCenter.db"
    RAMLimit = 64
    CPULimit = 18
