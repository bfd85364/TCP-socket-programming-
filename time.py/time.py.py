import socket # socket 모듈 
import time   # time 모듈

#TCP 소켓을 생성 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #soket 객체(class) 생성 (soket.AF_INET->IPv4, soket.SOCK_STREAM->TCP)
address=('localhost', 9999) # 서버의 주소와 포트번호=9999
server_socket.bind(address)  # 서버의 주소와 포트번호를 바인딩(소켓의 메소드->server_soket으로 연결해준다)
server_socket.listen(5)      #연결대기 -> 최대 5개의 클라이언트를 받아들일 수 있음

while True:
    client_socket, addr = server_socket.accept() # 연결허용 반환되는 값은 총2개-> 클라이언트 소켓, 상대방의 remote주소: TPV4, 포트(client socket, rem_addr) 반환 
    print("connect from ", addr) # 클라이언트의 주소 출력
    client_socket.send(time.ctime().encode()) # 클라이언트


    client_socket.close() # 클라이언트 소켓을 닫음

