import os
import subprocess

def alfaview_is_opened(proc):
    ps = subprocess.Popen("ps -A", shell=True, stdout=subprocess.PIPE)
    ps_pid = ps.pid
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    output = output.decode('utf-8')

    for line in output.split("\n"):
        if line != "" and line != None:
            fields = line.split()
            pid = fields[0]
            pname = fields[3]

            if(pname == proc):
                return True
    return False
