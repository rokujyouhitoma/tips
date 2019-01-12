import json
import unittest
import urllib
import urllib.request
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


class Test(unittest.TestCase):
    def setUp(self):
        url = 'http://localhost:8000/'
        host = 'localhost'
        port = 8000
        self.server = ThreadedHTTPServer(host, port, request_handler=MyHTTPRequestHandler)
        print("Start...: {}".format(url))
        self.server.start()
        print("Running")

    def tearDown(self):
        print("Stop...")
        self.server.stop()
        print("Stoped")

    def test_get(self):
        with urllib.request.urlopen('http://localhost.:8000/') as f:
            data = f.read().decode("utf8")
            obj = json.loads(data)
            print(obj)
            self.assertTrue(obj.get("client").get("command") == "GET")

if __name__ == '__main__':
    unittest.main()
