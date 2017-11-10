import paramiko as pm
from settings import *

class Assberry:
    def __init__(self, ip, port, user, password, cmd):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.cmd = cmd
        self.logged_in = False
        self.ssh = pm.SSHClient()
        self.ssh.set_missing_host_key_policy(pm.AutoAddPolicy())

    def login(self):
        self.ssh.connect(self.ip, self.port, self.user, self.password)

    def command(self, cmd):
        self.ssh.exec_command(cmd)



