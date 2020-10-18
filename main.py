from pypresence import Presence
import psutil
import time

client_id = "765270886164201502"
RPC = Presence(client_id)

RPC.connect()

while True:  
    cpu_per = round(psutil.cpu_percent(),1) 
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    time.sleep(15)

while True: 
    time.sleep(15)