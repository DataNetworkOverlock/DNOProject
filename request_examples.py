from utils.usuarios import Usuarios
from utils.tests import Tests

if __name__ == '__main__':

    # PAYLOADS
    user = {
        'name': 'usuario nuevo',
        'username': 'y4567890',
        'password': 'clave nueva',
        'question': 'pregunta 11',
        'answer': 'respuesta 1'
    }

    username = 'usuario2'

    auth = {
        'username': username,
        'password': 'clave2'
    }

    test_payload = {
        'ip': '192.168.0.0',
        'date': '2023-12-10 01:13:15',
        'report': 'elreporte',
        'user': 'uuid2',
        'script': 'suid1'
    }

    # USUARIOS
    usuario = Usuarios()
    # usuario.create_user(user=user)
    sesion = usuario.login(auth)
    token = sesion['token']

    print('Sesión:', sesion, 'Token:', token)

    # TESTS
    test = Tests(token)
    new_test = test.create_test(test_payload)
    tests = test.get_tests_by_username(username)

    print('New test:', new_test)
    print('Tests:', tests)
