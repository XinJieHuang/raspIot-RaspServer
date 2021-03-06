import socket

class DS18B20:
    temperature = ''

    def __init__(self, deviceIp, deviceUuid, deviceName):
        self.ip = deviceIp
        self.uuid = deviceUuid
        self.name = deviceName


    def getTemp(self):
        self.temperature = self.connectWithDevice('getTemp')
        return self.temperature


    def getDeviceAttribute(self):
        try:
            device = {}
            device['uuid'] = self.uuid
            device['name'] = self.name

            deviceContent = []
            deviceContent1 = {}
            deviceContent1['type'] = 'text'
            deviceContent1['name'] = 'Temperature'
            deviceContent1['value'] = self.getTemp()

            deviceContent.append(deviceContent1)

            device['deviceContent'] = deviceContent
            return device
        except Exception:
            return None


    def connectWithDevice(self, cmd):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, 8085))
        s.sendall(cmd.encode())
        recvdata = s.recv(1024).decode()
        s.close()
        return recvdata
