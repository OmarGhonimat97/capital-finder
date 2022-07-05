from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_get(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        diction = dict(query_string_list)

        if 'country' in diction:
            country = diction['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()

            the_name = data[0]["capital"][0]
            message = "The capital of " + str(country) + " is " + str(the_name)
        elif 'capital' in diction:
            capital = diction['capital']
            url = 'https://restcountries.com/v2/capital/'
            r = requests.get(url + capital)
            data = r.json()

            the_name = data[0]["name"]
            message = str(capital) + " is the capital of " + str(the_name)
        else:
            message = "Please enter a country's name or a capital's name"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return

