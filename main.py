import flet as ft
import principal as pr
from pyairtable.formulas import match
import airtable as at

def main(page: ft.Page):

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

    def ingresar(e: ft.ControlEvent):
        usuario = txt_usuario.value.strip()
        password = txt_contra.value.strip()

        try:
            formula = match({"clave": usuario, "contra": password})
            registro = at.Usuario.first(formula=formula)

            if registro:
                page.clean()
                pr.main(page)
            else:
                page.open(ft.SnackBar(ft.Text("Credenciales incorrectas"), bgcolor="red", show_close_icon=True))
        except Exception as e:
            page.open(ft.SnackBar(ft.Text(f"Error: {e}"), bgcolor="orange", show_close_icon=True))

    # Configuración general
    page.theme_mode = "light"
    page.title = "Inicio de sesión"
    page.padding = 0
    page.spacing = 0

    # Imagen de fondo
    background = ft.Image(
        src="flogin.png",  # Tu imagen
        fit=ft.ImageFit.COVER,
        width=page.width,
        height=page.height
    )
    # Componentes de la página
    txt_usuario = ft.TextField(label="Username/Correo", width=250)
    txt_contra = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    login_card = ft.Container(
        width=350,
        height=450,
        border_radius=30,
        bgcolor="white",
        padding=30,
        content=ft.Column(
            [ 
                ft.Column([
                    ft.Icon(ft.Icons.PERSON, size=80, color="#fa9f42"),
                    ft.Text("Bienvenido", size=28, font_family="Raleway-Bold"),
                    ft.Text("al sistema de gestión de bioenergías de Tabasco", size=12, font_family="Raleway-Medium", text_align=ft.TextAlign.CENTER),
                ], spacing=2,horizontal_alignment="center"),
                ft.Container(height=20),
                txt_usuario,
                txt_contra,
                ft.FilledButton(
                    "Iniciar sesión",
                    width=250,
                    icon=ft.Icons.LOGIN,
                    color="white",
                     bgcolor="#fa9f42",
                    on_click=ingresar
                )
            ],
            horizontal_alignment="center",
            spacing=15
        )
    )

    # Layout
    content = ft.Row(
        [
            ft.Container(
                content=login_card, 
                expand=False, 
                alignment=ft.alignment.center,
                margin=ft.margin.only(left=80)
                ),
            ft.Container(expand=True)
        ],
        expand=True
    )

    # Stack para superponer imagen y login
    page.add(
        ft.Stack(
            [
                ft.Container(content=background, expand=True),
                content
            ],
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
