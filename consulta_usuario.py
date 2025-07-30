import flet as ft
import airtable as at
import principal as pr

def main(page: ft.Page):

    # Configuración de la página
    page.title = "Consultas"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 600
    page.appbar = ft.AppBar(
        title = ft.Text("Consulta de Usuarios en la nube"),
        center_title=True,
        leading = ft.Icon("cloud"),
        color = "white",
        bgcolor = "green"
    )

    #Tabla de usuarios
    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre completo")),
        ft.DataColumn(ft.Text("Es administrador")),
    ]
    filas = []
    datos = at.Usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra, color="white", selectable=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Checkbox(value=d.admin, disabled=True))
        fila = ft.DataRow([celda1,celda2,celda3,celda4])
        filas.append(fila)

    tbl_usuarios = ft.DataTable(encabezado, filas)
    
    page.add(tbl_usuarios)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)