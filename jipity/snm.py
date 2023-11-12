from http.server import SimpleHTTPRequestHandler, HTTPServer

# Create a custom request handler by subclassing SimpleHTTPRequestHandler
class CustomRequestHandler(SimpleHTTPRequestHandler):
    pass

# Create the server
server = HTTPServer(('localhost', 8000), CustomRequestHandler)

# Start the server
print('Server started at http://localhost:8000')
server.serve_forever()