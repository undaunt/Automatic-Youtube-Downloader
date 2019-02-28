import sys
import subprocess
import os

if __name__ == "__main__":
    #import AYD
    #AYD.start()
    pythonPath = sys.executable
    cmd = [pythonPath, os.path.join("./poetry", "bin", "poetry"), "run", "python", "AYD.py "]
    if sys.platform.startswith("win"):
        #print('Using Windows System Settings')
        subprocess.run(cmd, shell=True)
    else:
        sys.stdout.flush()
        proc = subprocess.call(cmd)
        if proc > 0:
            print("An error occurred with downloading poetry")
            exit(1)
