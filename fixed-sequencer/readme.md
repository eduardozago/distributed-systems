## Group Communication with Fixed Sequencer

Group communication using tasks and message queue

The algorithm works as follows:
1. Sender group 
    i. Tasks generate a message that is placed on the queue
    ii. Messages are randomly generated numbers with a time they were generated (here the timestamp generation was simulated for better visualization)

2. Sequencer 
    i. After the sender group sends the messages, they are received in the sequencer
    ii. The sequencer orders messages according to the timestamp at which the message was created

2. Receiver group 
    i. The receiver group receives the messages and processes them as ordered by the sequencer

To execute:
```sh
python3 fixed_sequencer.py
```