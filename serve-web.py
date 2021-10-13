from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote


import logging
import json

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from urllib.parse import urlparse, parse_qs

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        o = urlparse(self.path)
        query = parse_qs(o.query)
        # logging.info(query)
        if query['x'] != "":
            x = query['x'][0]
            logging.info(x)
            x = json.loads(x)
            # logging.info(x[0][0])
            X = np.array(x)
            
            y = query['y'][0]
            logging.info(y)
            y = json.loads(y)
            # logging.info(y[0][0])
            y = np.array(y)
            
            p = query['predict'][0]
            # logging.info(p)
            p = json.loads(p)
            
            line_fitter = LinearRegression(fit_intercept=False)
            line_fitter.fit(X, y)

            hasil = line_fitter.predict(p)
            self.wfile.write("GET request for {}".format(hasil).encode('utf-8'))
        # if self.path != "":
            # self.path = json.loads(self.path)
        
        # X = np.array(self.path)
        # y = np.array([[10.7]])
        # plt.plot(X, y, 'o')
        # plt.show()

        # line_fitter = LinearRegression(fit_intercept=False)
        # line_fitter.fit(X, y)

        # hasil = line_fitter.predict([[13.6,13.6,37.6,30.5,61.9,61.9]])
        # print(hasil)
        # self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        # logging.info(self.path[0][0])  

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()