import json
import urllib
from http.server import SimpleHTTPRequestHandler

from threadedhttpserver import ThreadedHTTPServer


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    server_version = 'MyTestRequestServer'

    def version_string(self):
        return MyHTTPRequestHandler.server_version

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        parsed = urllib.parse.urlparse(self.path)
        query = parsed.query
        params = urllib.parse.parse_qs(query)
        data = {
            'client': {
                'command': self.command,
                'path': self.path,
                'query': query,
                'params': params,
                'request_version': self.request_version,
                'headers': dict(self.headers),
            },
            'server': {
                'server_version': self.server_version,
                'protocol_version': self.protocol_version,
            }
        }
        self.wfile.write(bytes(json.dumps(data), 'UTF-8'))


def main():
    url = 'http://localhost:8000/'
    host = 'localhost'
    port = 8000
    server = ThreadedHTTPServer(host, port, request_handler=MyHTTPRequestHandler)
    server.start()
    while True:
        pass

if __name__ == '__main__':
    main()
