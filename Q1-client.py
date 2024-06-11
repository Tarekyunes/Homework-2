import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12479))

    account_number = input("Enter your account number: ")
    client.send(account_number.encode())

    print(client.recv(1024).decode())

    while True:
        option = input("Enter option: ")
        if option == 'exit':
            break
        client.send(option.encode())

        if option == 'check balance':
            print(client.recv(1024).decode())
        elif option == 'deposit' or option == 'withdraw':
            amount = input("Enter amount: ")
            client.send(amount.encode())
            print(client.recv(1024).decode())

    client.close()


if __name__ == "__main__":
    main()