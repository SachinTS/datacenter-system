
from lib.resourceAlogrithm import findOptimalServer
#from someModule import fetchAllServer, updateServerInfo
from lib.AppLogger import get_reporting_logger
from lib.AppConstants import AppConstants



def updateServerInfo(serverID, cpuCore, ram, increase):
    pass

class ResourceManager(object):
    '''
        class to allocate server for given container.
    '''

    def __init__(self):
        self.logging = get_reporting_logger()
        self.container = AppConstants.CONTAINER


    def updateServerInfo(server, cores, ram, increase):
        '''
        function to update server RAM and CPU usage
        '''

        if increase:
            self.logging.info("increasing the CPU and RAM for server " + server)
            pass
        else:
            self.logging.info("decreasing the CPU and RAM for server " + server)
            pass

    def freeResource(self, container, serverID):
        self.updateServerInfo(serverID, self.container[containerType]['Cores'], self.container[containerType]['RAM'], False)

    def optimal_server(self, containerType):
        '''
        gets serverlist from DB
        makes use of algorithm to find optimal servers
        return server id on success
        or None on failure
        '''
        self.logging.info("fetching server info")
        try:
            serverList = self.fetchAllServer()
            self.logging.info(serverList)
        except Exception as e:
            self.logging.error("Fetching server list failed... :\s( ")
            self.logging.error(e)
        optimalServer = findOptimalServer(containerType, serverList)
        if not optimalServer:
            self.logging.error("No optimal servers found, returning None")
            return None
        elif optimalServer:
            # update CPU and RAM for serverCPULimit
            self.logging.info("Optimal server found. Returning")
            # print(ResourceManager.container[containerType]['Cores'])
            self.logging.info("Updating server info in DB")
            updateServerInfo(optimalServer, self.container[containerType]['Cores'], self.container[containerType]['RAM'], True)
            return optimalServer

    def fetchAllServer(self):
        serverInfo = {
            0:{"RAM":64,    "Cores":18, "Status":1},
            1:{"RAM":64,    "Cores":18, "Status":1},
            2:{"RAM":16,    "Cores":6,  "Status":1},
            3:{"RAM":4,    "Cores":1,  "Status":1},
            4:{"RAM":0,    "Cores":0,  "Status":0},
            5:{"RAM":0,    "Cores":0,  "Status":0}
            }
        return serverInfo
