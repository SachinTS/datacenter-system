# importing sqlite 3 for database operations
import sqlite3

# creating connection and cursor objects
con = sqlite3.connect('dataCenter.db')
c = con.cursor()


# systimeinc method to fetch minimum arrival time of the job which is waiting
def systimeinc():
    try:
        c.execute("select min(arrival_time) from jobs where status = 'WAITING'")
        arrival = c.fetchone()
    except Exception as e:
        print(str(e))
    # if there is a waiting job with minimum arrival time it will return
    # arrival time of that job, If no record then returns -1
    if not arrival[0]:
        return None
    else:
        return arrival[0]


# foreman function takes system time as an argument
def foreman(sys_time):
    # this function updates the jobs to status DONE whose current status is PROCESSING and
    # end_time is less than system time
    query = "update jobs set status='DONE' where status ='PROCESSING' and end_time<=" + str(sys_time)
    c.execute(query)
    con.commit()

    # this function selects job_id and container_type of the WAITING jobs whose arrival time
    # is less than or equal to system time
    query = "select job_id, container_type from jobs where arrival_time<= "+str(sys_time)+" and status='WAITING'"
    upcoming = c.fetchall()

    query = "update jobs set status='PROCESSING' where arrival_time<= "+str(sys_time)+" and status='WAITING'"
    c.execute(query)
    con.commit()

    if len(upcoming) == 0:
        return None
    else:
        return upcoming

def showall():
    c.execute("select * from jobs")
    data = c.fetchall()
    print(data)


min__arrival = systimeinc()
print(min__arrival)

result = foreman(90)
print(result)

showall()


c.close()
con.close()


