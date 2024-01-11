import time
import paramiko

HOST = '192.168.1.158'
USER = 'datanetworkoverlock'

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy (paramiko.AutoAddPolicy())

        password = 'DataOverLock1*'
        client.connect(HOST, username=USER, password=password)

        stdin, stdout, stderr = client.exec_command('ls')

        time.sleep(1)

        result = stdout.read().decode()

        print(result)

        client.close()
        
    except paramiko.ssh_exception.AuthenticationException as e:
        print ("error")