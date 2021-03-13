from flask import Flask

import ssl
import socket
import datetime


app = Flask(__name__)

hostnames=[
    "kubernetes",
    "prometheus-grafana"
]


@app.route("/")
def hello():
    resp=""
    for item in hostnames:
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=item,
        )

        conn.settimeout(3.0)
        conn.connect((item, 443))

        ssl_info = conn.getpeercert()
        resp = resp + item + " :" + "\n\t" + "Not Before: " +ssl_info['notBefore']+"\n\t" +"Not After : "+ssl_info['notAfter']+"\n"

    return resp

