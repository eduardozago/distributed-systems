import random
import time
import multiprocessing

def token_generator():
    token = random.randint(500, 599)
    return token

def run_process(data):
    print(f"Running {data[1]}\n")
    time.sleep(2)

def create_processes(token, num_processes):
    processes = []

    if num_processes == 1:
        id = 0
        message = "proccess " + str(id)
        next_task = None
        initial_token = token
        need_access = False

        data = [id, message, next_task, initial_token, need_access]

        processes.append(data)
    else:
        for i in range(num_processes):
            id = i
            message = "proccess " + str(id)
            next_task = i + 1

            if next_task == num_processes:
                next_task = 0

            if id == 0:
                initial_token = token
            else:
                initial_token = None
            
            need_access = False

            data = [id, message, next_task, initial_token, need_access]
            
            processes.append(data)

    return processes

def check_token(processes):
    process_token = None

    # checks if the token exists and returns the id of the process that has the token
    for i in range(len(processes)):
        if processes[i][3] != None:
            process_token = processes[i][3]
            return i

    # if there is no token between the processes, the token is assigned to the first process
    if process_token == None:
        process_token = token_generator()
        return 0

def check_processes(processes):    
    while True:
        # check that the token has not been lost
        process_token = check_token(processes)

        # print processes as the token is passed to the next process
        for i in range(len(processes)):
            #if the process failed it is removed
            if processes[i] == None:
                processes.pop(i)

            print(f"Process {i}: {processes[i]}")
        print("\n")

        # input of process request to run
        process_to_run = None

        if process_token == len(processes) // 2 or process_token == len(processes):
            process_to_run = input("Enter the process id to run (s to skip, q to quit): ")
            
            if process_to_run != "s" and process_to_run != "q":
                process_to_run = int(process_to_run)
                
                # set access request parameter
                if process_to_run >= 0 and process_to_run <= len(processes):
                    processes[process_to_run][4] = True
            print("\n")

            if process_to_run == "q":
                break
        
        # checks whether the process that has the token is requesting access
        if processes[process_token][4] == True:
            # run process
            process = multiprocessing.Process(target=run_process, args=(processes[process_token],))
            process.start()
            process.join()

            # set access request to false
            processes[process_token][4] = False

        # walks around the ring
        token = processes[process_token][3]
        processes[process_token][3] = None
        
        if (process_token + 1) == len(processes):
            processes[0][3] = token
            process_token = 0
        else:
            processes[process_token + 1][3] = token
            process_token += 1

        time.sleep(2)

def main():
    # input number of processes
    num_processes = input("Number of processes: ")
    num_processes = int(num_processes)

    # create token
    token = token_generator()

    # crate processes
    processes = create_processes(token, num_processes)

    # check processes to run in critical region
    check_processes(processes)

if __name__ == "__main__":
    main()