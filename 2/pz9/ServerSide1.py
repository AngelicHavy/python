import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


def today():
    today1 = datetime.datetime.today()
    return xmlrpc.client.DateTime(today1)


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(today, "today")
server.serve_forever()
