try:
    import usocket as socket
except:
    import socket

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Proyecto final: La barrera</h1>
    <span class="subtitulo">Descripcion:</span>
    <p></p>
    <span class="subtitulo">Estado actual:</span>
    <span class="estado"></span>
    <div class="botonera">
        <button type="button" class="boton">subir</button>
        <button type="button" class="boton" id="potato">bajar</button>
    </div>
    
</body>
</html>"""

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = ''
password = ''


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Conexion exitosa')
print(station.ifconfig())