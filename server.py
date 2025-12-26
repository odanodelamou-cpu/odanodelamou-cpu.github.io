from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 8000

print(f"Serveur lancé : http://localhost:{port}")

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
server.serve_forever()
