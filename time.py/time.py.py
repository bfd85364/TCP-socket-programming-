import socket # socket ��� 
import time   # time ���

#TCP ������ ���� 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #soket ��ü(class) ���� (soket.AF_INET->IPv4, soket.SOCK_STREAM->TCP)
address=('localhost', 9999) # ������ �ּҿ� ��Ʈ��ȣ=9999
server_socket.bind(address)  # ������ �ּҿ� ��Ʈ��ȣ�� ���ε�(������ �޼ҵ�->server_soket���� �������ش�)
server_socket.listen(5)      #������ -> �ִ� 5���� Ŭ���̾�Ʈ�� �޾Ƶ��� �� ����

while True:
    client_socket, addr = server_socket.accept() # ������� ��ȯ�Ǵ� ���� ��2��-> Ŭ���̾�Ʈ ����, ������ remote�ּ�: TPV4, ��Ʈ(client socket, rem_addr) ��ȯ 
    print("connect from ", addr) # Ŭ���̾�Ʈ�� �ּ� ���
    client_socket.send(time.ctime().encode()) # Ŭ���̾�Ʈ


    client_socket.close() # Ŭ���̾�Ʈ ������ ����

