import flet as ft
import airtable as at

def main(page: ft.Page):
    bioenergias = [] 

    def buscar_bioenergias(e):
        termino = txt_busqueda.value.lower()
        tabla.rows.clear()

        for u in bioenergias:
            if termino in u.cultivo.lower() or termino in u.parte.lower() or termino in u.municipio.lower():
                tabla.rows.append(
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(u.cultivo)),
                        ft.DataCell(ft.Text(u.parte)),
                        ft.DataCell(ft.Text(str(u.cantidad))),
                        ft.DataCell(ft.Text(str(u.humedad))),
                        ft.DataCell(ft.Text(str(u.area))),
                        ft.DataCell(ft.Text(str(u.energia))),
                        ft.DataCell(ft.Text(u.municipio)),
                        ft.DataCell(ft.Text(str(u.latitud))),
                        ft.DataCell(ft.Text(str(u.longitud)))
                    ])
                )
        page.update()

    def cargar_bio():
        nonlocal bioenergias
        bioenergias = at.Bioenergia.all()  # Se carga una sola vez
        for u in bioenergias:
            tabla.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(u.cultivo)),
                    ft.DataCell(ft.Text(u.parte)),
                    ft.DataCell(ft.Text(str(u.cantidad))),
                    ft.DataCell(ft.Text(str(u.humedad))),
                    ft.DataCell(ft.Text(str(u.area))),
                    ft.DataCell(ft.Text(str(u.energia))),
                    ft.DataCell(ft.Text(u.municipio)),
                    ft.DataCell(ft.Text(str(u.latitud))),
                    ft.DataCell(ft.Text(str(u.longitud)))
                ])
            )

    # Configuración visual
    page.title = "Consulta de Bioenergias"
    page.theme_mode = "light"
    page.fonts = {
        "Raleway-Regular": "Raleway-Regular.ttf",
        "Raleway-Medium": "Raleway-Medium.ttf",
        "Raleway-Bold": "Raleway-Bold.ttf"  
    }
    page.theme = ft.Theme(font_family="Raleway-Regular")
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 0

    # Imagen de fondo
    background = ft.Container(
        expand=True,
        content=ft.Image(
            src="consultabio.jpg",
            fit=ft.ImageFit.COVER,
            width=page.width,
            height=page.height
        )
    )

    txt_busqueda = ft.TextField(
        label="Buscar por cultivo, parte o municipio",
        prefix_icon="search",
        on_change=buscar_bioenergias,
        border_radius=30,
        expand=True
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Cultivo de origen", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Parte aprovechada del cultivo", font_family="Raleway-Bold" )),
            ft.DataColumn(label=ft.Text("Cantidad (t)", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Porcentaje de humedad (%)", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Área cultivada (ha)", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Contenido energético (MJ/kg)", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Municipio", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Latitud", font_family="Raleway-Bold")),
            ft.DataColumn(label=ft.Text("Longitud", font_family="Raleway-Bold")),
        ],
        rows=[]
    )

    principal = ft.Container(
        width=1000,
        height=400,
        bgcolor="white",
        border_radius=20,
        padding=30,
        content=ft.Column(
            [
                ft.Text("Consulta de Bioenergías", size=40, font_family="Raleway-Bold"),
                txt_busqueda,
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [tabla],
                                scroll=ft.ScrollMode.ALWAYS  # Scroll horizontal
                            )
                        ],
                        scroll=ft.ScrollMode.AUTO  # Scroll vertical
                    ),
                    expand=3,
                    bgcolor="white",
                    border_radius=5,
                    padding=5
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

    contenedor = ft.Row(
        [
            ft.Column(
                [principal],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        ft.Stack(
            [
                background,
                contenedor
            ],
            expand=True 
        )
    )

    cargar_bio()
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)