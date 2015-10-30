import socket

target_host = "itakoh.co.jp"
target_port = 80

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send("GET / HTTP/1.1\r\nHost: itakoh.co.jp\r\n\r\n")
    response = client.recv(4096)
    client.close()
    print(response)

main()
