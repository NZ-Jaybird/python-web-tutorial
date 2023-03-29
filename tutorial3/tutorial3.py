import json
from http.server import BaseHTTPRequestHandler, HTTPServer

sizes = ["S", "M", "L", "XL"]
colours = ["white", "brown", "grey", "black"]
garments = ["shirt", "hoodie", "trousers", "scarf"]

items = []

for size in sizes:
    for colour in colours:
        for garment in garments:
            items.append({"size": size, "colour": colour, "garment": garment})


class HttpServer(BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path == "/items.json":
            s.send_response(200)
            s.send_header("Content-type", "application/json")
            s.send_header('Access-Control-Allow-Origin', '*')
            s.end_headers()
            s.wfile.write(bytes(json.dumps(items, indent=4), "utf-8"))
        else:
            s.send_response(404)
            s.end_headers()


server = HTTPServer(("", 1202), HttpServer)
server.serve_forever()
