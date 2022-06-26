from time import sleep
import random
import requests
import os
from threading import Thread
import ast

worker_id = os.getenv('WORKER_NAME')
worker_id = int(worker_id)

clock = 0
jeton_present = False

if worker_id == 1:
    jeton_present = True


in_section = False
jeton = 10*[0]
request_vector = 10*[0]


def send_status(token, req, has_token, in_cs):
    data = {'token': token, 'req': req, 'has_token': has_token, 'in_cs': in_cs}
    headers = {"Content-type": "application/json"}
    requests.post("http://172.17.0.1:8000/post/"+str(worker_id)+"/", headers=headers, json=data)


sleep(10)


def critical_section():
    delta = random.randint(4, 5)
    sleep(delta)


def send_token(token, p):
    data = {"token": token}
    headers = {"Content-type": "application/json"}
    requests.post("http://172.17.0.1:810"+str(p)+"/worker/", headers=headers, json=data)


def diffusion(clock_p, j):
    data = {"j": j, "clock": clock_p}
    headers = {"Content-type": "application/json"}
    for i in range(10):
        if i != worker_id-1:
            requests.post("http://172.17.0.1:810"+str(i)+"/req/", headers=headers, json=data)


def wait_token():
    f = open('token', 'r+')
    token = ''
    print('waiting...')
    while token == '':
        token = f.read()
        token = token.split("\n")[0]
        sleep(0.1)
    f.close()
    open('token', 'w').close()
    return ast.literal_eval(token)['token']


# After ending CS routine
def after_section():
    global jeton_present
    jeton[worker_id - 1] = clock

    print(request_vector, "  ", jeton)

    for i in range(worker_id - 1, 10, 1):
        if i + 1 == worker_id:
            continue

        if (request_vector[i] > jeton[i]) and jeton_present:
            jeton_present = False
            send_token(jeton, i)
            print('token sent!')

    for i in range(0, worker_id - 1, 1):
        if i + 1 == worker_id:
            continue

        if (request_vector[i] > jeton[i]) and jeton_present:
            jeton_present = False
            send_token(jeton, i)
            print('token sent!')
    send_status(jeton, request_vector, jeton_present, in_section)


# receiving requests to enter CS
def receiver():
    global request_vector
    global jeton
    global in_section
    global jeton_present
    global clock

    print('receiving reqs...')
    while True:
        with open('req', 'r') as r:
            lines = r.readlines()
        for line in lines:
            if line != '':
                line = line.split("\n")[0]
                req = ast.literal_eval(line)
                print(req)
                j = req['j']
                h = req['clock']
                request_vector[j] = max(request_vector[j], h)
                send_status(jeton, request_vector, jeton_present, in_section)
                if jeton_present and not in_section:
                    after_section()

        r.close()
        open('req', 'w').close()
        sleep(0.05)


receiver = Thread(target=receiver)
receiver.daemon = True
receiver.start()

while True:
    send_status(jeton, request_vector, jeton_present, in_section)
    print('starting...')
    time = random.randint(5, 15)
    sleep(time)

    if not jeton_present:
        clock += 1
        diffusion(clock, worker_id-1)
        jeton = wait_token()
        jeton_present = True

    print('entering CS...')
    send_status(jeton, request_vector, jeton_present, in_section)

    in_section = True
    critical_section()
    in_section = False

    send_status(jeton, request_vector, jeton_present, in_section)

    sleep(2)

    print('CS done')

    after_section()




