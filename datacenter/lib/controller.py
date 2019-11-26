def SysTimeInc():
    #return next arrival_time of waiting job or -1
    print("The next job(s) arrive at ", 85)
    return 85

def f_waiting(sys_time):
    #return list[[int job_id][char container_type]] of all
    #waiting jobs with arrival_time <= sys_time
    list_waiting_jobs = [(100245, "A"),(100246, "C"),(100247, "D"),(100248, "C"),]
    print("The waiting jobs are : ", list_waiting_jobs)
    return list_waiting_jobs

def f_done(sys_time):
    #return list[[int server_id][char container_type]] of all
    #done jobs with end_time <= sys_time
    list_done_jobs = [(434275, "A"),(434276, "C"),(434277, "D"),(434278, "C"),]
    print("The done jobs are : ", list_done_jobs)
    return list_done_jobs

def AckAllocation(job_id, server_id):
    #send allocation of job and get 1, 0 or -1.
    return 1

def LeastArrTime():
    #return next end_time of processing job or -1
    print("There is no more waiting job, and the nex end_time of processing job is ", 120)
    return 120

def freeResource(id_server, container_type):
    print("Server ", id_server, " has been released from a ", container_type,"-type container.")
    return 1

def place_this_job(container_type):
    id_server = 434255
    print("This job has been placed in server ", id_server)
    return id_server

sys_time = 82
print("Sys_time = ", sys_time)
sys_time = SysTimeInc()
print("Sys_time = ", sys_time)
list_waiting_jobs = f_waiting(sys_time)

sys_time = 0
next_arrival_time = 0

print("\n\n------------ Let's begin -----------------\n\nSys_time = ", sys_time)

next_arrival_time = SysTimeInc()

while next_arrival_time != -1:
    sys_time = next_arrival_time
    list_done_jobs = f_done(sys_time)
    for elt in list_done_jobs:
        print(" --- ", elt)
        freeResource(elt[0], elt[1])


        #AckAllocation(optimalServer(elt),



    next_arrival_time = -1



   # next_arrival_time = SysTimeInc()
