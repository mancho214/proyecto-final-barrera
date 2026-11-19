const botones = document.querySelectorAll(".boton")

botones.forEach(boton => boton.addEventListener("click", (event) => {
    event.preventDefault();

    const accion = boton.getAttribute("data-accion")

    console.log(accion)

    const url = windows.location.href.split('/update?')[0];
    document.location.href = url + '/update?' + accion;
}))