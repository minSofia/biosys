import flet as ft
import airtable as at

def main(page: ft.Page):

    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra_2 = txt_contra2.value
        nombre = txt_nombre.value
        #Validar campos
        if clave == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor = "orange")
            page.open(snackbar)
            return
        if contra == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor = "orange")
            page.open(snackbar)
            return
        if contra_2 == "":
            snackbar = ft.SnackBar(ft.Text("Confirma tu contraseña"), bgcolor = "orange")
            page.open(snackbar)
            return
        if nombre == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu nombre"), bgcolor = "orange")
            page.open(snackbar)
            return

        # Confirmar contraseña
        if contra != contra_2:
            snackbar = ft.SnackBar(ft.Text("Contraseñas incorrectas"), bgcolor = "red")
            page.open(snackbar)
            return

        # Guardar el usuario en la nube
        nuevo = at.Usuario(
            clave=clave,
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value
        )
        try:
            nuevo.save()
            snackbar = ft.SnackBar(ft.Text("Usuario registrado"), bgcolor = "blue", show_close_icon=True)
            page.open(snackbar)
        except Exception as error:
            snackbar = ft.SnackBar(ft.Text(error), bgcolor="red", show_close_icon=True)
        
    def limpiar_formulario():
        clave.value = ""
        contra.value = ""
        contra_2.value = ""
        nombre.value = ""
        admin.value = ""
        page.update()


    #Configuración de la página
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
    
    page.title = "Alta de Usuario"
    page.scroll = "auto"
    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 35
    
    encabezado = ft.Container(
        ft.Text(
            "Agregar nueva usuario",
            size=40,
            color="#008b51",
            font_family="Raleway-Bold",
        ),
        padding=ft.padding.only(bottom=40)
    )
    
    #Componentes de la pagina
    txt_clave =ft.TextField(label="Clave del usuario", width=750, border_radius=30)
    txt_contra =ft.TextField(label="Contraseña", password = True, width=750, border_radius=30)
    txt_contra2 =ft.TextField(label="Confirmar contraseña", password = True, width=750, border_radius=30)
    txt_nombre =ft.TextField(label="Nombre completo", width=750, border_radius=30)
    chk_admin =ft.Checkbox(label="¿Es administrador?")

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
            on_click=guardar_usuario,
            width=600,
            height=40,
        )
    )

    formulario = ft.Column(
        controls=[
            encabezado, 
            txt_clave, 
            txt_contra, 
            txt_contra2, 
            txt_nombre, 
            ft.Container(chk_admin, width=750),
            btn_guardar
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=15
    )
    
    
    principal = ft.Container(
        content=formulario,
        alignment=ft.alignment.center,
        expand=True
    )

    page.add(ft.Container(content=principal, expand=True, alignment=ft.alignment.center))
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
