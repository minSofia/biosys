import flet as ft
import principal as pr

def main(page: ft.Page):
    page.title = "Registro de Biomasa"
    page.window_width = 900
    page.window_height = 700
    page.scroll = "auto"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    titulo = ft.Text("Registro de", size=20)
    subtitulo = ft.Text("Biomasa", size=36, weight="bold")

    cultivo_origen = ft.Dropdown(
        label="Cultivo de origen",
        options=[
            ft.dropdown.Option("Caña de azúcar"),
            ft.dropdown.Option("Cacao"),
            ft.dropdown.Option("Maíz"),
            ft.dropdown.Option("Coco"),
            ft.dropdown.Option("Platáno"),
        ],
        width=600
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
        width=600
    )

    cantidad = ft.TextField(label="Cantidad (t)", width=300)
    humedad = ft.TextField(label="Porcentaje de humedad (%)", width=300)
    area = ft.TextField(label="Área cultivada (ha)", width=300)
    contenido_energetico = ft.TextField(label="Contenido energético (MJ/kg)", width=300)

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
        width=600
    )

    latitud = ft.TextField(label="Latitud", width=300)
    longitud = ft.TextField(label="Longitud", width=300)

    btn_guardar = ft.FilledButton(
        "Guardar registro",
        icon=ft.Icons.SAVE,
        bgcolor="green",
        color="white",
        width=450
    )

    # Agrupar títulos y campos en columnas con alineación izquierda
    analisis_section = ft.Column(
        [
            ft.Text("Análisis Cuantitativo", size=20, weight="bold"),
            ft.Row([cantidad, humedad], alignment="center"),
            ft.Row([area, contenido_energetico], alignment="center")
        ],
        alignment="start",
        horizontal_alignment="start",
        width=600
    )

    ubicacion_section = ft.Column(
        [
            ft.Text("Ubicación", size=20, weight="bold"),
            municipio
        ],
        alignment="start",
        horizontal_alignment="start",
        width=600
    )

    coordenadas_section = ft.Column(
        [
            ft.Text("Coordenadas", size=16),
            ft.Row([latitud, longitud], alignment="center")
        ],
        alignment="start",
        horizontal_alignment="start",
        width=600
    )

    formulario = ft.Column(
        [
            titulo,
            subtitulo,
            cultivo_origen,
            parte_aprovechada,
            analisis_section,
            ubicacion_section,
            coordenadas_section,
            btn_guardar,
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=15
    )

    page.add(formulario)

if __name__ == "__main__":
    ft.app(target=main)