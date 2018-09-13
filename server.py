#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import requestParser
import json


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        data = requestParser.ParseGet(self)

        self._set_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=True))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        data = requestParser.ParsePost(self)

        self._set_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=True))
        
def run(server_class=HTTPServer, handler_class=Server, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port ' + str(port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
