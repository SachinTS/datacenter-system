import random
from lib.resourceManager import ResourceManager
from lib.DB_Connect import foreman_done, foreman_waiting, least_arr_time, least_end_time, ack_allocation
from lib.AppLogger import get_reporting_logger
logging = get_reporting_logger()

rm = ResourceManager()

def main():
    logging.info("__ Initialization of the variables __")
    sys_time = 0 #--------#
    logging.info(" | Sytem time = %d", sys_time)
    next_arrival_time = 0
    logging.info(" | There is no next arrival time yet")

    logging.info("__ Entering the Main Loop __")
    next_arrival_time = least_arr_time() #--------#
    if next_arrival_time:
        logging.info(" | First arrival time = %d", next_arrival_time)
    while next_arrival_time != None:
        #----------------------------------------#
        sys_time = next_arrival_time
        logging.info(" | Sytem time = %d", sys_time)
        list_done_jobs = foreman_done(sys_time)
        if list_done_jobs:
            logging.info(" | There is %d jobs that are now finished", len(list_done_jobs))
            logging.info("__ Freeing of the Resources __")
            for elt in list_done_jobs:
                logging.info(" | --> Server %d can erase a %c-type container", elt[0], elt[1])
                rm.freeResource(elt[1], elt[0]) #(containerType, server_id)#
        else:
            logging.info(" | There is no jobs finished yet")
        #----------------------------------------#
        list_waiting_jobs = foreman_waiting(sys_time)
        if list_waiting_jobs:
            logging.info(" | There is %d jobs to send to servers", len(list_waiting_jobs))
            logging.info("__ Allocation of the jobs __")
            for elt in list_waiting_jobs:
                logging.info(" | --> Job %d needs a %c-type container", elt[0], elt[1])
                alloc = rm.optimal_server(elt[1])
                if alloc:
                    logging.info(" | <-- Job %d has been allocated to server %s", elt[0], alloc)
                    ack_allocation(elt[0], alloc)
                else:
                    logging.info(" | <-- Job %d is an error", elt[0])
                    ack_allocation(elt[0], 0, True)
        else:
            logging.info(" | There is no more waiting jobs")
        next_arrival_time = least_arr_time() #--------#

    next_end_time = 0
    logging.info("__ Exiting slowly the program __")
    next_end_time = least_end_time()
    if next_end_time:
        logging.info(" | Next end time in the table = %d", next_end_time)
    while next_end_time != None:
        sys_time = next_end_time #--------#
        logging.info(" | Sytem time = %d", sys_time)
        list_done_jobs = foreman_done(sys_time) #--------#
        if list_done_jobs:
            logging.info(" | There is %d jobs that are now finished", len(list_done_jobs))
            logging.info("__ Freeing of the Resources __")
            for elt in list_done_jobs:
                logging.info(" | --> Server %d can erase a %c-type container", elt[0], elt[1])
                rm.freeResource(elt[1], elt[0]) #--------#
        next_end_time = least_end_time() #--------#
    logging.info(" | There is no more processing jobs")
    logging.info(" ")
    logging.info(" . . .")
    logging.info(" ")
    logging.info("      !!! CONGRATULATIONS !!!")
