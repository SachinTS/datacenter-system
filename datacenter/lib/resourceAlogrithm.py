import random
import unittest
from lib.AppConstants import AppConstants
from lib.AppLogger import get_reporting_logger


# creating connection and cursor objects
# con = sqlite3.connect(AppConstants.DB_FILE)
# c = con.cursor()

logging = get_reporting_logger()
# assumptions
# jobs of type [A,B,C,D]
# servers are stored as dictionaries

# RAM and CPU capacity of servers


# Array of servers keyed by address servers[0][RAM] returns
# the current RAM load of server 0 etc.
# only the currently powered servers are added to the array
# it's assummed that this is the format of the server data

#   RAM             Cores       Server
#   Allocated       Allocated   Status (Active/Idle)
'''
servers = {
    0:{"RAM":62,    "Cores":15, "Status":1},
    1:{"RAM":60,    "Cores":12, "Status":1},
    2:{"RAM":32,    "Cores":8,  "Status":1},
    3:{"RAM":16,    "Cores":6,  "Status":1},
    4:{"RAM":0,     "Cores":0,  "Status":0},
    5:{"RAM":0,     "Cores":0,  "Status":0},
    6:{"RAM":0,     "Cores":0,  "Status":0},
    7:{"RAM":0,     "Cores":0,  "Status":0},
    8:{"RAM":0,     "Cores":0,  "Status":0},
    9:{"RAM":0,     "Cores":0,  "Status":0}
}
'''


def findOptimalServer(job, servers):
    # the function will take a local search like approach
    # feasible, already powered, server addresses will be added to an array
    # the server chosen should be the one with the lowest evaluation
    # if no already powered server is feasible then one will be powered
    # at random and the job will be allocated

    # some information known prior

    RAMLimit = AppConstants.RAMLimit
    CPULimit = AppConstants.CPULimit

    types = AppConstants.CONTAINER

    # parameters:
    # job is a one letter code referring to the type of container being requested
    # servers is an array containing the current statuses of the servers
    # types is an array of the current containers available to be instantiated

    # first isloate addresses currently active servers
    activeServers = [s for s in servers if servers[s]["Status"] == 1]

    # determine if there are any idle servers
    if len(servers) - len(activeServers) > 0:
        idleServers = True
    else:
        idleServers = False


    # isolate list of feasible servers
    feasibleServers = []

    for s in activeServers:
        if (servers[s]["RAM"] + types[job]["RAM"] <= RAMLimit) and (servers[s]["Cores"] + types[job]["Cores"] <= CPULimit):
            feasibleServers.append(s)

    # evaluation is as follows:
    # a servers evaluation is the sum of its unused resources
    # 1 GB ram unused is 1 unused resource
    # 1 cpu core unused is one unused resource
    # the objective is to search through the list of feasible servers and evaluate
    # for each server, s, the sum of unused resources
    # the optimal server is the server with the smallest evaluation

    evaluations = []

    for s in feasibleServers:
        RAM = RAMLimit - (servers[s]["RAM"] + types[job]["RAM"])
        CPU = CPULimit - (servers[s]["Cores"] + types[job]["Cores"])

        evaluation = RAM + CPU

        evaluations.append(evaluation)

    # if two servers have the same evaluation the algorithm takes the first
    try:
        optimalServer = feasibleServers[evaluations.index(min(evaluations))]
    except:
        if idleServers:
            optimalServer = random.choice([s for s in servers if servers[s]["Status"] == 0])
            logging.info(" turning on idle server !!!!!!")
        else:
            return(None)

    return(optimalServer)
