# importing sqlite 3 for database operations
import sqlite3
from lib.AppConstants import AppConstants
from lib.ServerDB import initialiseDB, terminateDB
from lib.AppLogger import get_reporting_logger


# creating connection and cursor objects
# con = sqlite3.connect(AppConstants.DB_FILE)
# c = con.cursor()

logging = get_reporting_logger()


# systimeinc method to fetch minimum arrival time of the job which is waiting
def sys_time_inc():
    try:
        con, c = initialiseDB()
        c.execute("select min(arrival_time) from jobs where status = 'WAITING'")
        arrival = c.fetchone()
        terminateDB(con)
    except Exception as e:
        logging.error(str(e))
    # if there is a waiting job with minimum arrival time it will return
    # arrival time of that job, If no record then returns -1
    if not arrival[0]:
        return None
    else:
        return arrival[0]


# foreman function takes system time as an argument
def foreman_done(sys_time):
    # this function selects server_id and container_type of the PROCESSING jobs whose arrival time
    # is less than or equal to system time
    con, c = initialiseDB()
    c.execute("select server_id, container_type from jobs where end_time<= " + str(sys_time) +" and status='PROCESSING'")
    upcoming = c.fetchall()
    # print(upcoming)

    # this function updates the jobs to status DONE whose current status is PROCESSING and
    # end_time is less than system time
    query = "update jobs set status='DONE' where end_time<= " + str(sys_time) + " and status='PROCESSING'"
    c.execute(query)
    con.commit()
    terminateDB(con)
    if len(upcoming) == 0:
        return None
    else:
        return upcoming


# foreman_waiting function takes system time as an argument
def foreman_waiting(sys_time):
    # this function selects job_id and container_type of the jobs whose arrival time
    # is equal to system time
    con, c = initialiseDB()
    c.execute("select job_id, container_type from jobs where arrival_time = " + str(sys_time))
    waiting = c.fetchall()
    terminateDB(con)

    if len(waiting) == 0:
        return None
    else:
        return waiting


# ack_allocation function takes system time as an argument
def ack_allocation(job_id, server_id, error=False):
    if not error:
        query = "update jobs set server_id ='" + str(server_id) + "', status = 'PROCESSING' where job_id = '" + str(job_id) + "'"
    else:
        query = "update jobs set server_id ='" + str(server_id) + "', status = 'ERROR' where job_id = '" + str(job_id) + "'"
    try:
        con, c = initialiseDB()
        c.execute(query)
        con.commit()
        terminateDB(con)
        return
    except Exception as e:
        logging.error(str(e))


# least_arr_time function returns upcoming task
def least_arr_time():
    con, c = initialiseDB()
    c.execute("select * from jobs where status = 'WAITING'")
    waiting = c.fetchall()

    if len(waiting) == 0:
        return None
    else:
        c.execute("select min(arrival_time) from jobs where status = 'WAITING'")
        arrival = c.fetchone()
        terminateDB(con)
        if not arrival[0]:
            return None
        else:
            return arrival[0]


# foreman function takes system time as an argument
def foreman(sys_time):
    # this function updates the jobs to status DONE whose current status is PROCESSING and
    # end_time is less than system time
    con, c = initialiseDB()
    c.execute("select server_id, container_type from jobs where end_time<= " + str(sys_time) +" and status='PROCESSING'")
    upcoming = c.fetchall()

    query = "update jobs set status='PROCESSING' where arrival_time<= "+str(sys_time)+" and status='WAITING'"
    c.execute(query)
    con.commit()
    terminateDB(con)

    if len(upcoming) == 0:
        return None
    else:
        return upcoming

def showall():
    con, c = initialiseDB()
    c.execute("select * from jobs")
    data = c.fetchall()

    print(data)


#min__arrival = systimeinc()
#print(min__arrival)

#result = foreman(90)
#print(result)

#showall()


    terminateDB(con)
    logging.info(data)


# min__arrival = systimeinc()
# print(min__arrival)
#
# result = foreman(90)
# print(result)
#
# showall()
#
#
# c.close()
# con.close()
