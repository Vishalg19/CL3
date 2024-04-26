import xmlrpc.server

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def create_server(i):
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000 + i))
    server.register_function(factorial)
    print(f"Server started on http://localhost:{8000 + i}")
    server.serve_forever()

n = int(input("Enter the number of servers: "))
for i in range(n):
    create_server(i)