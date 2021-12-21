from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query_dict = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        end_time = datetime.strptime(query_dict["end_time"], r"%Y-%m-%d %H:%M:%S.%f")

        count = 0
        while datetime.now() < end_time:
            count += 1

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(count).encode())