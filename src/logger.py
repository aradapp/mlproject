import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# In order to create the log file override the logging

logging.basicConfig(
    filename=LOG_FILE_PATH,
    #this is just a custom format and can be changed
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #for which level you want to print message
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started")