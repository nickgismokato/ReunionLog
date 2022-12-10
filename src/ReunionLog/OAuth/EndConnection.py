import os
import sys

def EndConnection():
    if os.path.exists(".credentials.json"):
        os.remove(".credentials.json")
        print("Terminated Successfully")
    else:
        print("Could not terminate .credentials.json")