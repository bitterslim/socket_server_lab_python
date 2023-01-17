class Request:
    def __init__(self, file):
        self.file = file
        self.method = ''
        self.url = ''
        self.protocol = ''
        self.headers = {}
        self.body = None
        self.parse_request_line()
        self.parse_headers()
        self.parse_body()

    def parse_request_line(self):
        request_line = self.read_line()
        self.method, self.url, self.protocol = request_line.split()
        if self.protocol != 'HTTP/1.1':
            raise ValueError('ERROR, wrong protocol')
    
    

    def parse_headers(self):
        while True:
            header = self.read_line()
            if header == '':
                break
            name, value = header.split(': ')
            self.headers[name] = value

    def parse_body(self):
        content_length = self.headers.get("Content_length")
        if content_length:
            self.body = self.file.read(int(content_length))

    def read_line(self):
        return self.file.readline().decode().strip()


