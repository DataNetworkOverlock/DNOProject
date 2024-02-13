import time
import paramiko


class ExecCommand:

    def __init__(self):
        self.HOST = '192.168.1.239'
        self.USER = 'datanetworkoverlock'
        self.RUTA = "/home/datanetworkoverlock/Escritorio/SCRIPTS"

    def exec(self, payload):
        nombre_script = payload["nombre_script"]
        parametros = ""

        for key, value in payload["parameters"].items():
            parametros += value + " "

        comando = f".{self.RUTA}/{nombre_script}.sh {parametros}"

        try:
            password = 'DataOverLock1*'
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname=self.HOST,
                           username=self.USER,
                           password=password)

            stdin, stdout, stderr = client.exec_command(comando)
            time.sleep(1)
            result = stdout.read().decode()

            client.close()

            return result

        except paramiko.ssh_exception.AuthenticationException as e:
            print("error")
