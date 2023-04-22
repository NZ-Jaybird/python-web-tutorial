La intención de estos ejercicios de aprendizaje es progresar a través de maneras como estructurar una aplicación web. Los ejercicios tienen un tema fácil de comercio electrónico - solo una página mostrando productos.


-- Ejercicio 1 --

Ejercicio 1 es una pagina web estatica. Usa HTML y CSS básico hacer una página que muestra productos con algunas características diferentes. Por ejemplo, he usado diferentes tipos de ropa, con diferentes tallas y colores. Intentar escribir el mismo HTML y CSS para cada producto entonces extraemos una plantilla para el ejercicio 2.


-- Ejercicio 2 --

Escribe un guión de Python que genera cada combinación de las características de los productos que usted creó en el ejercicio 1. Hacer que el código python escriba todos estos datos en un archivo Javascript entonces la página web puede leer y mostrar estos. El método de HTML body.onload() puede transformar las características de productos a HTML y escribe esa en el documento de HTML.


-- Ejercicio 3 --

Usando el código de una biblioteca de python - http.server, es posible crear un servidor http mínimo. Es decir, un programa que responde a solicitudes http, por ejemplo una página web siendo exhibido en el navegador. En este ejercicio, el servidor http escucha solicitudes a http://localhost:1202/items.json y devuelve los datos del producto en formato json. Entonces la página web puede solicitar los datos del producto en javascript en lugar de tener que cargar un archivo javascript separado. Usa el Fetch API de javascript.


-- Ejercicio 4 --

Extienda el servidor http para devolver el archivo html para solicitudes a http://localhost:1202/. En lugar de abrir el archivo html en tu navegador, abre la url http://localhost:1202/ en tu navegador. Luego, en lugar de un punto final que vuelve los datos json, genera html por los productos con python. Reemplazar el punto final items.json por solo un punto final productos, es decir,  http://localhost:1202/items que devuelve ese fragmento html. Luego, actualizar tu javascript para obtener ese fragmento html y lo inserta en el documento.


-- Ejercicio 5 --

En este ejercicio, añadir lógica del lado del cliente rastrear cantidad por cada producto. Añadir html a la plantilla de producto que muestra una etiqueta y valor para cantidad, y dos botones que aumentan y disminuyen respectivamente la cantidad de ese producto. Añadir un controlador de clics de javascript a estos botones que cambian el cantidad adecuadamente.

Nota que porque los valores sólo almacenados en javascript, ellos serán restablecidos si la página está refrescada.


-- Ejercicio 6 --

Primero, mueve la lógica de cantidad al lado del servidor. Luego, cambia los controladores de clics de los botones de cantidad para enviar una solicitud al servidor. La solicitud debe incluir información sobre qué producto está cambiando y cómo su cantidad está cambiando. Añadir un controlador en el servidor http de python que procesa la solicitud y almacena las cantidades en una variable o lista. Actualizar cómo se genera el html cuando la página es solicitada, para que se incluyan las últimas cantidades.

Deberías ahora puedes actualizar las cantidades en la página y refrescar la página sin que esas cantidades desaparezcan. Sin embargo, si el programa de python es reiniciado y la página es refrescada, las cantidades serán borradas.


-- Ejercicio 7 --

Este último ejercicio utilizará una base de datos. Puedes usar mysql o cualquier otra base de datos pero yo he usado postgres. Instale el software de la base de datos. Para postgres, abra la interfaz web de pgAdmin y siga estas instrucciones para configurar un usuario, una base de datos y una tabla para el ejercicio.
     - Cree el usuario 'shop_tutorial' con la contraseña 'tutorial' y permiso de iniciar sesión
     - Crear una nueva base de datos 'shop', asignando al nuevo usuario 'shop_tutorial' como propietario
     - Cree una nueva tabla 'item', en el esquema público en la base de datos 'shop' usando este script: CREAR TABLA elemento(item_id varchar, integer);

Para controlar esta base de datos desde el script de python, utilicé la biblioteca de python psycopg. Instalarlo con `pip install psycopg`. Vea los documentación aquí: https://www.psycopg.org/docs/usage.html

En el manipulador http de python para actualizaciones de cantidad, se necesita una consulta de inserción de sql si no hay un registro todavía para el producto, de lo contrario, una consulta de actualización de sql. Al comienzo de la secuencia de comandos de python, lea las cantidades de la base de datos para que esto está listo para la carga primera de la página.

Comienza el sitio web y añade algunas cantidades. Detener y comenzar el script de Python luego actualice la página web. Las cantidades deberían seguir siendo las mismas ahora porque fueron grabadas y cargadas desde la base de datos.
