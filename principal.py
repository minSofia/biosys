import flet as ft
import alta_usuario as nu
import consulta_usuario as cu
import registro_biomasa as nb
import consulta_bioenergia as bio

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

    def mostrar_nuevo(e: ft.ControlEvent):
        page.clean()
        nu.main(page)

    def mostrar_consulta(e: ft.ControlEvent):
        page.clean()
        cu.main(page)

    def mostrar_nueva_bio(e: ft.ControlEvent):
        page.clean()
        nb.main(page)

    def mostrar_bioenergias(e: ft.ControlEvent):
        page.clean()
        bio.main(page)

    #Configuración de la página
    page.title = "Menú principal"
    page.theme_mode= "light"
    page.padding = 28

    encabezado = ft.Column([
            ft.Text("Sistema de Gestión de Bioenergías", size=70, color="#008b51", font_family="Raleway-Bold"),
            ft.Text("Transformando recursos en energía para un mañana sostenible", size=28, font_family="Raleway-Medium"),
        ],
        alignment="center",
        horizontal_alignment= "center",
        spacing = 5
    )

    content = ft.Container(
        content=encabezado,
        alignment=ft.alignment.center,
        margin=ft.margin.only(bottom=20)
    )

    tar_imagen1 = ft.Container(
        border_radius=20,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Stack([
            ft.Image(
                src="bioenergia.jpg",
                width=float("inf"),
                height=float("inf"),
                fit=ft.ImageFit.COVER
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(
                    "Agregar bioenergía",
                    size=40,
                    font_family="Raleway-Medium",
                    color="white",
                ),
                on_click=mostrar_nueva_bio
            )
        ])
    )

    tar_grad1 = ft.Container(
        border_radius=20,
        alignment=ft.alignment.center,
        gradient=degradado,
        content=ft.Text(
            "Consultar bioenergía",
            size=40,
            font_family="Raleway-Medium",
            color="white"
        ),
        on_click=mostrar_bioenergias
    )

    fila1 = ft.Row(
    controls=[
        ft.Container(tar_imagen1, expand=2),
        ft.Container(tar_grad1, expand=1)
    ],
    spacing=10,
    alignment="center",
    vertical_alignment="stretch",
    expand=True
)

    tar_grad2 = ft.Container(
        border_radius=20,
        alignment=ft.alignment.center,
        gradient=degradado,
        content=ft.Text(
            "Consultar usuario",
            size=40,
            font_family="Raleway-Medium",
            color="white"
        ),
        on_click=mostrar_consulta
    )

    tar_imagen2 = ft.Container(
        border_radius=20,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Stack([
            ft.Image(
                src="usuario.jpg",
                width=float("inf"),
                height=float("inf"),
                fit=ft.ImageFit.COVER
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(
                    "Agregar nuevo usuario",
                    size=40,
                    font_family="Raleway-Medium",
                    color="white",
                ),
                on_click=mostrar_nuevo
            )
        ])
    )

    fila2 = ft.Row(
        controls=[
            ft.Container(tar_grad2, expand=1),
            ft.Container(tar_imagen2, expand=2)
        ],
        spacing=10,
        alignment="center",
        vertical_alignment="stretch",
        expand=True 
    )


    #Añadir a la página
    page.add( content, fila1, fila2)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)