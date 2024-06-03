import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("\nMessage from server:", message)
        except Exception as e:
            print("Error receiving message:", e)
            break


def send_message():
    while True:
        message = input("Enter message: ")
        if message == 'exit':
            break
        client.send(message.encode('utf-8'))


print("Connected to server.")

while True:
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    if not send_message():
        break

client.close()
