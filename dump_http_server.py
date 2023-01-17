from os import path
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
from request import Request

class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)
        print(f'Method - {request.method}')
        print(f'URL - {request.url}')
        print(f'Protocol - {request.protocol}')
        print(f'Header - {request.headers}')
        print(f'Body - {request.body}')

        response_body = self.get_response_body(request.url)
        response_body_len = len(response_body.encode())
        response = [
            'HTTP/1.1 200 OK',
            f'Content-Type: {self.get_content_type(request.url)}',
            'Content-Length: ' + str(response_body_len),
            'Connection: close',
            '',
            response_body
        ]

        self.wfile.write('\r\n'.join(response).encode())


    def get_response_body(self, url):
        file = self.get_file_path(url)
        if path.exists(file):
            with open(f'{file}', 'r') as file:
                response_body = file.read()
        else:
            response_body = f'<h4>404 Not Found</h1><a href="/">Home</a>'
        return response_body


    def get_file_path(self, url: str):
        if url == "/":
            return "templates/index.html"
        url = url.lstrip('/')
        if url.endswith(".css"):
            return f"styles/{url}"
        else:
            return f"templates/{url}.html"
        
        
    def get_content_type(self, url):
        if ".css" in url:
            return "text/css"
        else:
            return "text/html"



class ThreatedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "localhost", 8000

TCPServer.allow_reuse_address = True

with ThreatedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()