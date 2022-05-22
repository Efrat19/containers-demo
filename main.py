from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHTTP(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Welcome to Containers Class</h1>")

server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CustomHTTP)
server_object.serve_forever()