from time import sleep
from servo import Servo

barrera = Servo(Pin(25))

def webpage():
    html = '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-family:Tahoma;
        }

        body{
            background-color: rgb(191, 240, 236);
        }

        .botonera {
            gap: 10px;
        }

        .boton{
            padding: 15px 60px;
            border-radius: 6px;
            border-style: none;
            background-color: rgb(224, 218, 88);
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Proyecto final: La barrera</h1>
    <span class="subtitulo">Descripcion:</span>
    <p></p>
    <span class="subtitulo">Estado actual:</span>
    <span class="estado"></span>
    <div class="botonera">
        <button type="button" class="boton" data-accion="1">subir</button>
        <button type="button" class="boton" data-accion="0">bajar</button>
    </div>
    <script>
        const botones = document.querySelectorAll(".boton")

        botones.forEach(boton => boton.addEventListener("click", (event) => {
            event.preventDefault();

            const accion = boton.getAttribute("data-accion")

            console.log(accion)

            const url = window.location.href.split('/update?')[0];
            document.location.href = url + '/update?' + accion;
        }))
    </script>
</body>
</html>
        '''
    return html

def obtener_parametros(request):
    try:
        request = request.decode('utf-8')
    except:
        pass

    lineas = request.split(' ')
    linea_correcta = None
    for linea in lineas:
        if '/update?' in linea:
            linea_correcta = linea
            break

    if not linea_correcta:
        return None
    
    query = linea_correcta.split('/update?', 1)[1][0]
    
    return query

def mover_barrera(direccion):
    if direccion = {1}
    barrera.write_angle(90) 
if direccion = {0}
    barrera.write_angle(0) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print(f'Entro una conexion desde {str(addr)}')
    request = conn.recv(1024)
    request = str(request)
    print(f'Contenido = {request}')

    parametros = obtener_parametros(request)
    print (f"Accion: {parametros}")

    mover_barrera(int(parametros))

    response = webpage()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type text/html\n')
    conn.send('Conecction: close\n\n')
    conn.sendall(response)
    conn.close()