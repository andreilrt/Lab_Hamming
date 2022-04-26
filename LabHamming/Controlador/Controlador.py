Mensaje = [[]]
FPs = []
Trama = ''
Check = ''

class Controlador:
    def setMensaje(self, mensaje):
        global Mensaje
        Mensaje = mensaje

    def getMensaje(self):
        return Mensaje

    def setFPs(self, fps):
        global FPs
        FPs = fps
    
    def getFPs(self):
        return FPs

    def setTrama(self, trama):
        global Trama
        Trama = trama
    
    def getTrama(self):
        return Trama

    def setCheck(self, check):
        global Check
        Check = check
    
    def getCheck(self):
        return Check
