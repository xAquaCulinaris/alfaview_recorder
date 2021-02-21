import psutil

process_name = 'alfaview'


def getPID(process_name):
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return proc.pid
    return None


def killProcess(pid):
    process = psutil.Process(pid)
    process.terminate()
    print('Alfaview has been closed')

def close_alfaview():
    print('trying to close alfaview')
    pid = getPID(process_name)
    if pid == None:
        print("Alfaview hase been already closed")
    else:
        killProcess(pid)
