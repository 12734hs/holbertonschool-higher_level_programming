import http.server
import socketserver
import json

dict_sample = {"name": "John", "age": 30, "city": "New York"}
json_sample = json.dumps(dict_sample)


sub = http.server.SimpleHTTPRequestHandler

class Handler(sub):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)  # статус 200 OK
            self.send_header("Content-type", 'text/plain')  # тип ответа
            self.end_headers()  # конец заголовков
            self.wfile.write(b'Hello, this is a simple API!')  # тело ответа (байты!)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_sample.encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_error(404, 'Endpoint not found')

PORT = 8000
server = socketserver.TCPServer(('', PORT), Handler)
server.serve_forever()
