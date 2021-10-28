import socket
import base64

def udp_echo_service():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind(('0.0.0.0',12345))

    data,address = s.recvfrom(4096)
    print(data, address)
    s.sendto(data,address)


def udp_echo_client():
    s = socket.socket(type=socket.SOCK_DGRAM)
    data = b'No, I am John Davis'
    s.sendto(data,('192.168.243.1',12345))
    print('waiting for an echo')
    echodata,address = s.recvfrom(4096)
    print(echodata, address)

def tcp_echo_service():
    s = socket.socket()
    s.bind(('',12345))
    s.listen()
    while True:
        conn, address = s.accept()
        data = conn.recv(4096)
        print('recieved', data)
        conn.send(data)
        print('replied')

def tcp_echo_client():
    s = socket.socket()
    s.connect(('192.168.243.1',12345))
    print('Connection succeeded')

    data = b'hello'
    s.send(data)
    print(data, ' sent')
    #echodata = s.recv(4096)
    #print(data, ' recieved')

def qotd(server = '129.6.15.30', port=13):
    s = socket.socket()
    s.connect((server,port))

    msg = bytearray()
    chunk = s.recv(32)
    while chunk:
        msg.extend(chunk)
        chunk = s.recv(32)

    return msg

def malware(server = '10.50.30.236', port=12345):
    
    
    s = socket.socket()
    s.connect((server,port))

    msg = bytearray()
    chunk = s.recv(32)
    while chunk:
        msg.extend(chunk)
        chunk = s.recv(32)

    return msg




if __name__ == '__main__':
    msg = malware()
    print(base64.b64decode(msg))

