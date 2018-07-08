import socketserver
import threading
from http.server import SimpleHTTPRequestHandler


class ThreadedHTTPServer(object):
    def __init__(self, host, port, request_handler=SimpleHTTPRequestHandler):
        socketserver.TCPServer.allow_reuse_address = True
        self.server = socketserver.TCPServer((host, port), request_handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()

    def start(self):
        self.server_thread.start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
