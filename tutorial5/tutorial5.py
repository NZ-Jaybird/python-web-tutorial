from http.server import BaseHTTPRequestHandler, HTTPServer

sizes = ["S", "M", "L", "XL"]
colours = ["white", "brown", "grey", "black"]
garments = ["shirt", "hoodie", "trousers", "scarf"]

itemHtml = ""
itemId = 10000001


def initialUpper(str):
    return str[:1].upper() + str[1:]


for size in sizes:
    for colour in colours:
        for garment in garments:
            itemHtml += (
                '<div class="item" id="item%d">'
                "    <b>Garment:</b> %s"
                "    <br />"
                "    <b>Colour:</b> %s"
                "    <br />"
                "    <b>Size:</b> %s"
                "    <br />"
                '    <b>Quantity:</b> <span class="quantity">0</span>'
                "    <br />"
                '    <button onclick="add(%d)">+</button>'
                '    <button onclick="remove(%d)">-</button>'
                "</div>"
            ) % (
                itemId,
                initialUpper(garment),
                initialUpper(colour),
                size,
                itemId,
                itemId,
            )
            itemId += 1


class HttpServer(BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path == "/":
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            with open("tutorial5.html", "rb") as htmlFile:
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
