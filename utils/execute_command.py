import os
import time
import paramiko
from dotenv import load_dotenv


class ExecCommand:

    def __init__(self):
        load_dotenv()
        self.HOST = os.getenv("HOST")
        self.USER = os.getenv("USER")
        self.RUTA = os.getenv("PATH")

    def exec(self, payload):
        nombre_script = payload["nombre_script"]
        ruta_script = payload["source"]
        parametros = ""

        for key, value in payload["parameters"].items():
            parametros += value + " "

        comando = f"{ruta_script} {parametros}"
        print("Comando: "+comando)

        try:
            password = os.getenv("PASSWORD")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname=self.HOST,
                           username=self.USER,
                           password=password)

            stdin, stdout, stderr = client.exec_command(comando)

            time.sleep(1)
            result = stdout.read().decode()
            print("Resultado: "+result)

            client.close()

            return result

        except paramiko.ssh_exception.AuthenticationException as e:
            print("error")
        except paramiko.ssh_exception.SSHException as ee:
            print("ssh error")
