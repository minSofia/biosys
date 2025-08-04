import flet as ft
import principal as pr
from pyairtable.formulas import match
import airtable as at

def main(page: ft.Page):

    def ingresar(e: ft.ControlEvent):
        usuario = txt_usuario.value.strip()
        password = txt_contra.value.strip()

        try:
            formula = match({"clave": usuario, "contra": password})
            registro = at.Usuario.first(formula=formula)

            if registro:
                print("¡Funciona!")
                page.clean()
                pr.main(page)
            else:
                print(f"Usuario '{usuario}' no encontrado.")
                snackbar = ft.SnackBar(ft.Text("Credenciales incorrectas"), bgcolor="red", show_close_icon=True)
                page.open(snackbar)
            
            
        except Exception as e:
            print(f"Error de Airtable: {e}")
            snackbar = ft.SnackBar(ft.Text(f"Ocurrió un error al guardar: {e}"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)

        
    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesión"
    page.window.width = 800
    page.window.height = 600

    # Componentes de la página
    logo = ft.Icon("person", size=100, color="pink")
    txt_bienvenido = ft.Text("Bienvenida", size=30)
    txt_usuario = ft.TextField(label="Username/Correo", width=250)
    txt_contra = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    btn_login = ft.FilledButton(
        "Iniciar sesión",
        width=250,
        icon=ft.Icons.LOGIN,
        color="white",
        bgcolor="pink",
        on_click=ingresar
    )

    page.add(logo, txt_bienvenido, txt_usuario, txt_contra, btn_login)
    page.update()

# Inicio de la aplicación
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
