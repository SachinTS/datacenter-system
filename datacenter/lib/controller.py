import random
from lib.resourceManager import ResourceManager
from lib.DB_Connect import systimeinc, showall
from lib.AppLogger import get_reporting_logger
logging = get_reporting_logger()

rm = ResourceManager()

def fake_optimal_server(containerType):
    server_id = random.randint(1,9)
    logging.info(" | <-- Well received : %c-type container sent to server %d", containerType, server_id)
    return server_id

def fake_freeResource(server_id, containerType):
    logging.info(" | <-- Well received : Server %d erase a %c-type container", server_id, containerType)
    return 1

def fake_least_arrival_time():
    #return next arrival_time of waiting job or -1
    least_arrival_time = 85
    logging.info(" | The next arrival_time of processing job is %d", least_arrival_time)
    return least_arrival_time

def fake_foreman_waiting(sys_time):
    #return list[[int job_id][char container_type]] of all
    #waiting jobs with arrival_time <= sys_time
    list_waiting_jobs = [(852787, "D"),(852788, "A"),(852789, "B"),(852790, "C"),]
    print("The waiting jobs are : ", list_waiting_jobs)
    return list_waiting_jobs

def fake_foreman_done(sys_time):
    #return list[[int server_id][char container_type]] of all
    #done jobs with end_time <= sys_time
    list_done_jobs = [(434275, "A"),(434276, "C"),(434277, "D"),(434278, "C"),]
    print("The done jobs are : ", list_done_jobs)
    return list_done_jobs

def fake_ack_allocation(job_id, server_id):
    #send allocation of job and get 1, 0 or -1.
    return 1

def fake_least_end_time():
    #return next end_time of processing job or -1
    least_end_time = 120
    logging.info(" | The next end_time of processing job is %d", least_end_time)
    return least_end_time

def fake_place_this_job(container_type):
    id_server = 434255
    print("This job has been placed in server ", id_server)
    return id_server

def main():
    logging.info("__ Initialization of the variables __")
    sys_time = 0 #--------#
    logging.info(" | Sytem time = %d", sys_time)
    next_arrival_time = 0
    logging.info(" | There is no next arrival time yet")

    logging.info("__ Entering the Main Loop __")
    next_arrival_time = fake_least_arrival_time() #--------#
    logging.info(" | First arrival time = %d", next_arrival_time)
    while next_arrival_time != None:
        sys_time = next_arrival_time #--------#
        logging.info(" | Sytem time = %d", sys_time)
        list_done_jobs = fake_foreman_done(sys_time) #--------#
        logging.info(" | There is %d jobs that are now finished", len(list_done_jobs))
        logging.info("__ Freeing of the Resources __")
        for elt in list_done_jobs:
            logging.info(" | --> Server %d can erase a %c-type container", elt[0], elt[1])
            fake_freeResource(elt[0], elt[1]) #--------#
        list_waiting_jobs = fake_foreman_waiting(sys_time) #--------#
        logging.info(" | There is %d jobs to send to servers", len(list_waiting_jobs))
        logging.info("__ Allocation of the jobs __")
        for elt in list_waiting_jobs:
            logging.info(" | --> Job %d needs a %c-type container", elt[0], elt[1])
            alloc = fake_optimal_server(elt[1])
            if alloc != -1:
                logging.info(" | <-- Job %d has been allocated to server %d", elt[0], alloc)
                fake_ack_allocation(elt[0], alloc)
            else:
                logging.info(" | <-- Job %d is an error", elt[0])
                fake_ack_allocation(None)
        ###################
        next_arrival_time = None
        #next_arrival_time = fake_least_arrival_time() #--------#
        ###################
    logging.info(" | There is no more waiting jobs")
    next_end_time = 0
    logging.info("__ Exiting slowly the program __")
    next_end_time = fake_least_end_time()
    logging.info(" | Next end time in the table = %d", next_end_time)
    while next_end_time != None:
        sys_time = next_end_time #--------#
        logging.info(" | Sytem time = %d", sys_time)
        list_done_jobs = fake_foreman_done(sys_time) #--------#
        logging.info(" | There is %d jobs that are now finished", len(list_done_jobs))
        logging.info("__ Freeing of the Resources __")
        for elt in list_done_jobs:
            logging.info(" | --> Server %d can erase a %c-type container", elt[0], elt[1])
            fake_freeResource(elt[0], elt[1]) #--------#
        ###################
        next_end_time = None
        #next_end_time = fake_least_end_time() #--------#
        ###################
