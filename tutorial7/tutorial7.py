from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2

db_connection = "dbname=shop user=shop_tutorial password=tutorial"

sizes = ["S", "M", "L", "XL"]
colours = ["white", "brown", "grey", "black"]
garments = ["shirt", "hoodie", "trousers", "scarf"]
quantities = {}

conn = psycopg2.connect(db_connection)
cur = conn.cursor()
cur.execute("SELECT item_id, quantity FROM item")
for record in cur:
    print(record)
    print(record[0])
    print(record[1])
    quantities[record[0]] = record[1]
conn.commit()
cur.close()
conn.close()


def initialUpper(str):
    return str[:1].upper() + str[1:]


def getItemHtml():
    itemHtml = ""
    itemId = 10000001
    for size in sizes:
        for colour in colours:
            for garment in garments:
                if not itemId in quantities:
                    print(itemId)
                    quantities[itemId] = 0
                itemHtml += (
                    '<div class="item" id="item%d">'
                    "    <b>Garment:</b> %s"
                    "    <br />"
                    "    <b>Colour:</b> %s"
                    "    <br />"
                    "    <b>Size:</b> %s"
                    "    <br />"
                    '    <b>Quantity:</b> <span class="quantity">%d</span>'
                    "    <br />"
                    '    <button onclick="add(%d)">+</button>'
                    '    <button onclick="remove(%d)">-</button>'
                    "</div>"
                ) % (
                    itemId,
                    initialUpper(garment),
                    initialUpper(colour),
                    size,
                    quantities[itemId],
                    itemId,
                    itemId,
                )
                itemId += 1
    return itemHtml


def updateQuantity(itemId, quantity):
    quantities[itemId] = max(quantity, 0)
    conn = psycopg2.connect(db_connection)
    cur = conn.cursor()
    cur.execute("SELECT quantity FROM item WHERE item_id = %s", [itemId])
    if cur.fetchone():
        cur.execute(
            "UPDATE item SET quantity = %s WHERE item_id = %s",
            (quantities[itemId], itemId),
        )
    else:
        cur.execute("INSERT INTO item VALUES (%s, %s)", (itemId, quantities[itemId]))
    conn.commit()
    cur.close()
    conn.close()
    return quantities[itemId]


class HttpServer(BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path == "/":
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            with open("tutorial7.html", "rb") as htmlFile:
                s.wfile.write(htmlFile.read())
        elif s.path == "/items":
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes(getItemHtml(), "utf-8"))
        else:
            s.send_response(404)
            s.end_headers()

    def do_PUT(s):
        print(s.path)
        if s.path.startswith("/item/"):
            itemId = int(s.path[6:])
            print(itemId)
            quantity = int(s.rfile.read(int(s.headers["Content-Length"])))
            print(quantity)
            updatedQuantity = updateQuantity(itemId, quantity)
            print(updatedQuantity)

            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes(str(updatedQuantity), "utf-8"))


server = HTTPServer(("", 1202), HttpServer)
server.serve_forever()
