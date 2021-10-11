import requests
import json
import os
import smtplib
from email.message import EmailMessage


class Producto:
    def __init__(self, id, nombre, linkProducto, precio, imagen, idTienda, idUsuario, precioDeseado, listColores, colorDeseado):
        self.id = id
        self.nombre = nombre
        self.linkProducto = linkProducto
        self.precio = precio
        self.imagen = imagen
        #self.idTienda = idTienda
        #self.idUsuario = idUsuario
        #self.precioDeseado = precioDeseado
        #self.listColores = listColores[0]
        #self.nombreColor = self.listColores['nombreColor']
        #self.stockTalle = self.listColores['stockTalle']

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)


def devolverProductoConMayorPrecio(producto1, producto2):
    if producto1.precio > producto2.precio:
        mayorPrecio = producto1
    else:
        mayorPrecio = producto2
    return mayorPrecio


urlBase = os.environ.get('URL_API')

url1 = urlBase + "https://www.fullh4rd.com.ar/prod/17658/video-geforce-rtx-3080-10gb-pny-xlr8-epic-x-rgb-full-mineria"
url2 = urlBase + "https://www.fullh4rd.com.ar/prod/20610/video-geforce-rtx-3070-msi-ventus-3x-8gb-lhr"


json1 = requests.get(url1)
json2 = requests.get(url2)


string1 = json1.text
string2 = json2.text


producto1 = Producto.from_json(string1)
producto2 = Producto.from_json(string2)

mayorPrecio = devolverProductoConMayorPrecio(producto1, producto2)

emailAdress = os.environ.get('EMAIL_USER')
emailKey = os.environ.get('GMAIL_KEY')
contacts = ['themagnetteam@gmail.com', 'themagnetteam@gmail.com']

msg = EmailMessage()
msg['Subject'] = f'El producto {mayorPrecio.nombre} es mas caro valiendo ${mayorPrecio.precio}'
msg['From'] = emailAdress
msg['To'] = 'themagnetteam@gmail.com'


msg.add_alternative(f"""\
<!DOCTYPE html>
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
       <a href={mayorPrecio.linkProducto}>Ver producto</a>
    </body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(emailAdress, emailKey)
    smtp.send_message(msg)
