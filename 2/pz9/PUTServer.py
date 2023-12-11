from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


def put_data(data):
    print("Received PUT request with data:", data)
    return "PUT request successful"


server = SimpleXMLRPCServer(("localhost", 8080))
print("Listening on port 8080...")
server.register_function(put_data, 'put_data')
server.serve_forever()
