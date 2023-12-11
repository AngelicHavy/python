import xmlrpc.client

DATA = b'some data'
proxy = xmlrpc.client.ServerProxy("http://localhost:8080/")
result = proxy.put_data(DATA)

print("Result:", result)
