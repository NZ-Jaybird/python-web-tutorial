The intent of this tutorial series is to progress through different possible ways to structure a webapp. The tutorials use a simple ecommerce concept - a page displaying various products.


-- Tutorial 1 --

Tutorial 1 starts off this series with a static webpage. Using simple HTML and CSS, create a page that displays a few similar items that vary by a few properties. For example, I've used different types of clothes, each with a given size and colour. Try to use the same HTML and CSS for each item so that we can extract a template for them in Tutorial 2.


-- Tutorial 2 --

Using the properties for the items you created in Tutorial 1, write a python script that generates every possible combination of these properties. Write out the resulting items to a javascript file so that the webpage can read and display it. A javascript function run by the HTML body.onload() method could transform each item's properties into HTML and write that HTML into the document.


-- Tutorial 3 --

Using python library code from http.server, it is possible to create a minimal http server - that is, a program that responds to http requests, for example from a webpage being loaded in the browser. In this tutorial, the http server listens for requests to http://localhost:1202/items.json and returns the items in JSON format. This means the web page can request the item data in javascript instead of having to load a separate file. To do this, use the javascript Fetch API.


-- Tutorial 4 --

Extend the http server to return the html file for requests to http://localhost:1202/. Instead of opening the html file in your browser, open the URL http://localhost:1202/ in your browser. Next, instead of an endpoint that returns the JSON data, generate HTML for the items with python. Replace the items.json endpoint with just an items endpoint, i.e. http://localhost:1202/items which returns that HTML. Finally, update your javascript to fetch that HTML chunk and insert it directly into the document.


-- Tutorial 5 --

In this tutorial, add client side logic to track quantity for each item. Add HTML to the item template that displays a quantity label and value, and two buttons that respectively increase and decrease the quantity of that item. Add a javascript click handler to those buttons that changes the quantity value appropriately.

Note that because the values are stored only in javascript, they will be reset if the page is refreshed.


-- Tutorial 6 --

In this tutorial, move the quantity logic to the server side. Change the click handlers of quantity buttons to send a request to the server. The request should include information about which item is changing and how its quantity is changing. Add a handler in the python http server that processes the request and stores the quantities in some kind of variable or list. Update how the HTML is generated when the page is requested, so that the latest quantities are included.

You should now be able to update the quantities on the page and then refresh the page without those values being reset. However, if the python script is restarted and the page refreshed, the quantities will then be reset.


-- Tutorial 7 --

The last tutorial for now demonstrates the use of a database. You could use mysql or any other but I've used postgresql. The database software will need to be installed separately on your computer. I've then created a user, database and table for this tutorial using the following steps in the pgAdmin web UI.
 - Create user 'shop_tutorial', set password 'tutorial' and grant log in permission
 - Create a new database 'shop', assigning the new user 'shop_tutorial' as the owner
 - Create a new table 'item', under the public schema in database 'shop', using this script: CREATE TABLE item (item_id varchar, quantity integer);

To control this database from the python script, I've used the python library psycopg. Install with `pip install psycopg`. See the docs here: https://www.psycopg.org/docs/usage.html

In the python http handler for quantity updates, you'll need either a SQL insert query if there isn't a record yet for the item being updated, or a SQL update query if there is. When the python script first runs, initialize the quantity data from the database so that it's ready for the first page load.

Finally you should be able to run the python script and see the website. After updating a few quantities, restart the python script and reload the webpage. The quantities should be unchanged, having been persisted to and loaded back from the database.
