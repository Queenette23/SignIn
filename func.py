import threading
from time import sleep


from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Backend(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        
    authenticated = pyqtSignal(str, arguments=['_authenticate'])  
        
        
    @pyqtSlot(str, str)
    def authenticate(self, email, passcode):
        auth_thread = threading.Thread(target=self._authenticate,
        args=[email, passcode])
        auth_thread.daemon = True
        auth_thread.start()   
         
    def _authenticate(self, email, passcode):       
        
       sleep(5)
       print(email, passcode)
        