##  Distributed Mutual Exclusion with Token Ring

Process synchronization with token ring

The algorithm works as follows:
1. Creation of processes
    i. Processes are created in a quantity defined upon entry at the beginning of execution
    ii. Each process corresponds to the following structure:

    | Id | Message | Id next process | Need access |
    | -- | ------- | --------------- | ----------- |
    | 0 | "process 0" | 1 | False |

2. Process verification 
    i. After the sender group sends the messages, they are received in the sequencer
    ii. After the processes are created, the token starts going through the processes and checking if the "Need access" parameter is True
    iii. If the "Need access" parameter is True, the moment the token passes through the process it will execute it

3. Simulation
    i. As the token travels through the ring, inputs are provided to determine the process it needs to perform.

To execute:
```sh
python3 token-ring.py
```