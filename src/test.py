import ssl
import socket
import datetime

def ssl_expiry_datetime(host, port=443):

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=host,
    )

    conn.settimeout(3.0)
    conn.connect((host, port))

    ssl_info = conn.getpeercert()

    print(host + " :" + "\n\t" + "Not Before: " +ssl_info['notBefore']+"\n\t" +"Not After : "+ssl_info['notAfter'])

print(ssl_expiry_datetime("google.com"))

