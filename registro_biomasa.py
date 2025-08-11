import flet as ft
import airtable as at

def main(page: ft.Page):

    def guardar_bio(e):
        # Validar campos completos
        if not all([cultivo_origen.value, parte_aprovechada.value, cantidad.value, 
                   area.value, contenido_energetico.value, municipio.value,
                   latitud.value, longitud.value, humedad.value]):
            page.open(ft.SnackBar(ft.Text("Completa todos los campos para guardar"), bgcolor="red", show_close_icon=True))
            return

        try:
            # Guardar en Airtable 
            nuevo_registro = at.Bioenergia(
                cultivo=cultivo_origen.value,  
                parte=parte_aprovechada.value,     
                cantidad=float(cantidad.value),
                area=float(area.value),
                energia=float(contenido_energetico.value),
                municipio=municipio.value,  
                latitud=float(latitud.value),
                longitud=float(longitud.value),
                humedad=float(humedad.value),
            )
            nuevo_registro.save()
            page.open(ft.SnackBar(ft.Text("Registro guardado exitosamente"), bgcolor="green", show_close_icon=True))
            limpiar_formulario()
        except Exception as e:
            page.open(ft.SnackBar(ft.Text(f"Error: {e}"), bgcolor="orange", show_close_icon=True))

    def limpiar_formulario():
        cultivo_origen.value = None
        parte_aprovechada.value = None
        cantidad.value = ""
        area.value = ""
        contenido_energetico.value = ""
        municipio.value = None
        latitud.value = ""
        longitud.value = ""
        humedad.value = ""
        page.update()

    #Componentes de la página
    page.fonts = {
        "Raleway-Regular": "Raleway-Regular.ttf",
        "Raleway-Medium": "Raleway-Medium.ttf",
        "Raleway-Bold": "Raleway-Bold.ttf"  
    }

    page.theme = ft.Theme(font_family="Raleway-Regular")

    degradado = ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=["#008b51", "#75ba40"]
    )
    
    page.title = "Registro de Biomasa"
    page.scroll = "auto"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 35

    encabezado = ft.Container(
        ft.Text(
            "Agregar nueva bioenergía",
            size=40,
            color="#008b51",
            font_family="Raleway-Bold",
        ),
        padding=ft.padding.only(bottom=40)
    )

    cultivo_origen = ft.Dropdown(
        label="Cultivo de origen",
        options=[
            ft.dropdown.Option("Caña de azúcar"),
            ft.dropdown.Option("Cacao"),
            ft.dropdown.Option("Maíz"),
            ft.dropdown.Option("Coco"),
            ft.dropdown.Option("Plátano"),
        ],
        width=750,
        border_radius=30 
    )

    parte_aprovechada = ft.Dropdown(
        label="Parte aprovechada del cultivo",
        options=[
            ft.dropdown.Option("Hojas"),
            ft.dropdown.Option("Tallos"),
            ft.dropdown.Option("Cáscara"),
            ft.dropdown.Option("Bagazo"),
            ft.dropdown.Option("Rastrojo"),
        ],
        width=750,
        border_radius=30
    )

    cantidad = ft.TextField(label="Cantidad (t)", width=375, border_radius=30)
    humedad = ft.TextField(label="Porcentaje de humedad (%)", width=375, border_radius=30)
    area = ft.TextField(label="Área cultivada (ha)", width=375, border_radius=30)
    contenido_energetico = ft.TextField(label="Contenido energético (MJ/kg)", width=375, border_radius=30)

    municipio = ft.Dropdown(
        label="Municipio",
        options=[
            ft.dropdown.Option("Balancán"),
            ft.dropdown.Option("Cárdenas"),
            ft.dropdown.Option("Centla"),
            ft.dropdown.Option("Centro"),
            ft.dropdown.Option("Comalcalco"),
            ft.dropdown.Option("Cunduacán"),
            ft.dropdown.Option("Emiliano Zapata"),
            ft.dropdown.Option("Huimanguillo"),
            ft.dropdown.Option("Jalapa"),
            ft.dropdown.Option("Jalpa de Méndez"),
            ft.dropdown.Option("Jonuta"),
            ft.dropdown.Option("Macuspana"),
            ft.dropdown.Option("Nacajuca"),
            ft.dropdown.Option("Paraíso"),
            ft.dropdown.Option("Tacotalpa"),
            ft.dropdown.Option("Teapa"),
            ft.dropdown.Option("Tenosique"),
        ],
        width=750,
        border_radius=30
    )

    latitud = ft.TextField(label="Latitud", width=375, border_radius=30)
    longitud = ft.TextField(label="Longitud", width=375, border_radius=30)

    btn_guardar = ft.Container(
        width=600,
        height=40,
        border_radius=30,
        alignment=ft.alignment.center,
        gradient=degradado,
        margin=ft.margin.only(top=35),
        content=ft.TextButton(
            "Guardar registro",
            style=ft.ButtonStyle(
                color="white",
                bgcolor=None,
            ),
            icon=ft.Icons.SAVE,
            on_click=guardar_bio,
            width=600,
            height=40,

        )
    )

    analisis = ft.Column(
        [
            ft.Text("Análisis Cuantitativo", size=20, font_family="Raleway-Bold"),
            ft.Row([cantidad, humedad], alignment="center"),
            ft.Row([area, contenido_energetico], alignment="center")
        ],
        alignment="start",
        horizontal_alignment="start",
        width=750
    )

    ubicacion = ft.Column(
        [
            ft.Text("Ubicación", size=20, font_family="Raleway-Bold"),
            municipio
        ],
        alignment="start",
        horizontal_alignment="start",
        width=750
    )

    coordenadas = ft.Column(
        [
            ft.Text("Coordenadas", size=16),
            ft.Row([latitud, longitud], alignment="center")
        ],
        alignment="start",
        horizontal_alignment="start",
        width=750
    )

    formulario = ft.Column(
        [
            encabezado,
            cultivo_origen,
            parte_aprovechada,
            analisis,
            ubicacion,
            coordenadas,
            btn_guardar,
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=15
    )

    page.add(formulario)

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
