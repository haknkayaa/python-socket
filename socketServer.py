"""
    @title      :
    @date       : 2019
    @author     : Hakan Kaya
    @mail       : mail@hakankaya.kim
    @description: Socket Server

"""
import socket


def server_program():
    host = socket.gethostname()
    port = 5000

    print("Bu bilgisayar'ın hostname'i: " + str(host))
    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(3)

    conn, address = server_socket.accept()
    print("Server'a baglanan cihaz: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        print(str(address) + " adresinden gelen mesaj: " + str(data))
        message = "OK"
        conn.send(message.encode())
        """if not data:
            break
        # endif"""

        #message = input("Mesaj göndermek icin -> ")
        conn.send(message.encode())
    # end while

    conn.close()
# end def


if __name__ == '__main__':
    server_program()
# endif
