from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime, timedelta
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Example request: /api/counter_parent?duration_seconds=1
        query_dict = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        duration_seconds = int(query_dict["duration_seconds"])

        end_time = str(datetime.now() + timedelta(seconds=duration_seconds))

        url = f"https://serverless-chloenott.vercel.app/api/counter_child?end_time={end_time}"
        #url = f"http://localhost:3000/api/counter_child?end_time={end_time}"
        
        count = requests.get(url).text

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(count).encode())
