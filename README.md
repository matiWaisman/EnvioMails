# EnvioMails
Este script es una prueba del funcionamiento del envio de mails, cifrado de datos y pasaje de json a objetos en python, recibiendo dos links de productos, pasando por el backend y mediante el uso de HtmlAgilityPack convierto el link en un Json con los datos importantes del producto, como el precio, nombre, la imagen, etc..
Al no poder pasarles el backend completo porque hay muchas cosas que hay que emprolijar y tampoco poder pasarles las claves de los mails y datos del backend al estar encriptados les dejo un video donde se ve el funcionamiento: 


https://user-images.githubusercontent.com/83453393/136719176-5d7c4933-b04f-4e9b-bb9c-653503e4ca16.mp4


El objetivo final de este script es poder hacerlo una recurrent task en el servidor y que cada media hora recorra los productos que los usuarios subieron a la base de datos, y que compare el precio deseado del usuario con el del momento, si el producto bajo su precio se le enviaria un mail como mas o menos se ve aca. 
