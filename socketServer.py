"""
    @title      :
    @date       : 2019
    @author     : Hakan Kaya
    @mail       : mail@hakankaya.kim
    @description: Socket Server
    /version : information for version
    /close   : communatication close
    /help    : helping guide

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

        if data == "/version":
            message = "0.1"
            conn.send(message.encode())
        #endif

        elif data == "/help":
            message = "helping guide ...."
            conn.send(message.encode())

        elif data == "/close":
            conn.close()
        #endif

        else:
            message = "OK"
            conn.send(message.encode())
        #endelse

    # end while

    conn.close()
# end def


if __name__ == '__main__':
    server_program()
# endif
