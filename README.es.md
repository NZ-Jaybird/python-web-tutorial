La intención de estos ejercicios de aprendizaje es progresar a través de maneras como estructurar una aplicación web. Los ejercicios tienen un tema fácil de comercio electrónico - solo una página mostrando productos.


-- Ejercicio 1 --

Ejercicio 1 es una pagina web estatica. Usa HTML y CSS básico hacer una página que muestra productos con algunas características diferentes. Por ejemplo, he usado diferentes tipos de ropa, con diferentes tallas y colores. Intentar escribir el mismo HTML y CSS para cada producto entonces extraemos una plantilla para el ejercicio 2.


-- Ejercicio 2 --

Escribe un guión de Python que genera cada combinación de las características de los productos que usted creó en el ejercicio 1. Hacer que el código python escriba todos estos datos en un archivo Javascript entonces la página web puede leer y mostrar estos. El método de HTML body.onload() puede transformar las características de productos a HTML y escribe esa en el documento de HTML.


-- Ejercicio 3 --

Usando el código de una biblioteca de python - http.server, es posible crear un servidor http mínimo. Es decir, un programa que responde a solicitudes http, por ejemplo una página web siendo exhibido en el navegador. En este ejercicio, el servidor http escucha solicitudes a http://localhost:1202/items.json y devuelve los datos del producto en formato json. Entonces la página web puede solicitar los datos del producto en javascript en lugar de tener que cargar un archivo javascript separado. Usa el Fetch API de javascript.


-- Ejercicio 4 --

Extienda el servidor http para devolver el archivo html para solicitudes a http://localhost:1202/. En lugar de abrir el archivo html en tu navegador, abre la url http://localhost:1202/ en tu navegador. Luego, en lugar de un punto final que vuelve los datos json, genera html por los productos con python. Reemplazar el punto final items.json por solo un punto final productos, es decir,  http://localhost:1202/items que devuelve ese fragmento html. Luego, actualizar tu javascript para obtener ese fragmento html y lo inserta en el documento.
