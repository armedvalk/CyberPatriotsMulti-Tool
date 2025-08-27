import os
from vt-py import vt
client = vt.Client(VIRUS_TOTAL_KEY)
DIRECTORY_SCAN="C:\"
def DirScan():
  fileScan=vt.Client.scan_file(DIRECTORY_SCAN)
  analysis=client.scan_file(f,wait_for_completion=True)
  if(analysis.waitforcompletion==False):
    wait(30)
    print("Exited with code 40")
    break
    return(fileScan)
    
  
  
