"""
    @title      :
    @date       : 2019
    @author     : Hakan Kaya
    @mail       : mail@hakankaya.kim
    @description: Socket Client


"""
import socket


def client_program():
    host = "192.168.1.234"
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Mesajiniz -> ")
    client_socket.send(message.encode())

    while message.lower().strip() != "close":

        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)

        message = input("Mesajiniz -> ")
        client_socket.send(message.encode())

    #endwhile

    client_socket.close()


if __name__ == '__main__':
    client_program()
#endif