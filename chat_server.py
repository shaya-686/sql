import socket
import threading
import redis

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def handle_message(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        r.lpush('messages', message)
        print("Received:", message)
        for client in clients:
            if client_socket != client:
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print("Error sending message to", client, ":", e)
    client_socket.close()


print("Server is running...")
clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_message, args=(client_socket, client_address))
    client_thread.start()


