# importing sqlite 3 for database operations
import sqlite3
from lib.AppConstants import AppConstants
from lib.AppLogger import get_reporting_logger


logging = get_reporting_logger()
# creating connection and cursor objects
def initialiseDB():
    con = sqlite3.connect(AppConstants.DB_FILE)
    c = con.cursor()
    return con, c

def terminateDB(con):
    con.close()

def fetchAllServer():
    logging.info("Reading all server info from DB")
    try:
        con, c = initialiseDB()
        c.execute("select * from servers")
    except Exception as e:
        print(str(e))
    data = c.fetchall()
    terminateDB(con)
    logging.info("Returning all servers info")
    return data


def updateServerInfo(serverID, cpuCore, ram, increase):
    con, c = initialiseDB()
    if increase:
        logging.info("increasing RAM and CPU for server:" + serverID)
        # new_ram =
        try:
            query = "UPDATE servers SET RAM_Used = RAM_Used + "+ str(ram) +" , CPU_Used = CPU_Used + " \
                     + str(cpuCore) + " WHERE id = " + serverID
            logging.info("executing query: " + query)
            c.execute(query)
            con.commit()
        except Exception as e:
            logging.error(str(e))

    else:
        try:
            logging.info("decreasing RAM and CPU for server:" + serverID)
            query = "UPDATE servers SET RAM_Used = RAM_Used - "+ str(ram) +" , CPU_Used = CPU_Used - " \
                     + str(cpuCore) + " WHERE id = " + serverID
            logging.info("executing query: " + query)
            c.execute(query)
            con.commit()

        except Exception as e:
            logging.error(str(e))
    terminateDB(con)
    return
    # c.execute("select * from servers")
    # values = c.fetchall()
    # print(values)
