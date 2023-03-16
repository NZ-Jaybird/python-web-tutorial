from http.server import BaseHTTPRequestHandler, HTTPServer

sizes = ["S", "M", "L", "XL"]
colours = ["white", "brown", "grey", "black"]
garments = ["shirt", "hoodie", "trousers", "scarf"]

itemHtml = ""


def initialUpper(str):
    return str[:1].upper() + str[1:]


for size in sizes:
    for colour in colours:
        for garment in garments:
            itemHtml += (
                '<div class="item">'
                "    <b>Garment:</b> %s"
                "    <br />"
                "    <b>Colour:</b> %s"
                "    <br />"
                "    <b>Size:</b> %s"
                "</div>"
            ) % (initialUpper(garment), initialUpper(colour), size)


class HttpServer(BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path == "/":
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            with open("tutorial4.html", "rb") as htmlFile:
                s.wfile.write(htmlFile.read())
        elif s.path == "/items":
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes(itemHtml, "utf-8"))
        else:
            s.send_response(404)
            s.end_headers()


server = HTTPServer(("", 1202), HttpServer)
server.serve_forever()
