import sqlite3
import random
from lib.ServerDB import initialiseDB, terminateDB

def jobGeneration(n):

    containerTypes = ['A','B','C','D']
    con, c = initialiseDB()
    query = "DELETE FROM jobs WHERE 1 = 1;"
    c.execute(query)
    con.commit()
    terminateDB(con)

    arrivalTime = 0
    for i in range(n):
        requestType = ''.join(random.choices(containerTypes, [0.6, 0.2, 0.1, 0.1]))
        requestTime = random.randint(0,20) + random.randint(0,20) + random.randint(0,20)
        arrivalTime = random.randint(0,20) + arrivalTime
        con, c = initialiseDB()
        query = "INSERT INTO jobs (job_id, Container_type, status, Duration, Arrival_time) VALUES('" + str(i) + "', '" + str(requestType) + "', 'WAITING', '" + str(requestTime) + "', '" + str(arrivalTime)+ "');"
        c.execute(query)
        con.commit()
        terminateDB(con)

    con, c = initialiseDB()
    query = "UPDATE jobs SET end_time = (duration + arrival_time) WHERE 1 = 1;"
    c.execute(query)
    con.commit()
    terminateDB(con)

    print("Job Generation is done.")
