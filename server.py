from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Устанавливаем путь к корневой директории для сервера
        self.directory = os.path.dirname(os.path.abspath(__file__))
        super().do_GET()

# Настройки сервера
PORT = 8000
server_address = ('', PORT)

# Запуск сервера
httpd = HTTPServer(server_address, MyHandler)
print(f"Сервер запущен на http://localhost:{PORT}")
httpd.serve_forever()
