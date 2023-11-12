# Define the root directory
root_dir = "C:/Users/Nibeza Kevin/Desktop/jipity/"



import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the path to the folder
folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "jipity")

# Ensure the folder exists, if not, create it
os.makedirs(folder_path, exist_ok=True)

# Define a custom request handler to handle CRUD operations
class CustomRequestHandler(SimpleHTTPRequestHandler):
    
      def do_GET(self):
        file_path = os.path.join(folder_path, self.path[1:])
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')
    
        def do_PUT(self):
            file_path = os.path.join(folder_path, self.path[1:])
            content_length = int(self.headers['Content-Length'])
            with open(file_path, 'wb') as f:
                f.write(self.rfile.read(content_length))
            self.send_response(201)
            self.end_headers()

        def do_DELETE(self):
            file_path = os.path.join(folder_path, self.path[1:])
            if os.path.exists(file_path):
                os.remove(file_path)
                self.send_response(200)
            else:
                self.send_response(404)
            self.end_headers()

# Create the server
server = HTTPServer(('localhost', 8000), CustomRequestHandler)

# Start the server
print('Server started at http://localhost:8000')
server.serve_forever()
