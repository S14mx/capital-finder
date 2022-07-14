from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        url = "https://restcountries.com/v2/"

        if "country" in dic:
            r = requests.get(url + "name/" + dic["country"])
            data = r.json()
            message = "The capital of " + \
                data[0]["name"] + " is " + data[0]["capital"]

        if "capital" in dic:
            r = requests.get(url + "capital/" + dic["capital"])
            data = r.json()
            message = data[0]["capital"] + \
                " is the capital of " + data[0]["name"]

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
