import flet as ft
import alta_usuario as nu
import consulta_usuario as cu

def main(page: ft.Page):

    def mostrar_nuevo(e: ft.ControlEvent):
        page.clean()
        nu.main(page)

    def mostrar_consulta(e: ft.ControlEvent):
        page.clean()
        cu.main(page)

    #Configuración de la página
    page.title = "Menú principal"
    page.theme_mode= "light"
    page.appbar = ft.AppBar(
        title= ft.Text("Sistema de Gestión de Bioenergías"),
        leading= ft.Icon("energy_savings_leaf"),
        color= "white",
        bgcolor= "purple",  
    )

    btn_nuevo = ft.ElevatedButton("Agregar nuevo usuario", on_click=mostrar_nuevo)
    btn_consultas = ft.ElevatedButton("Consultar usuarios", on_click=mostrar_consulta)
    #Añadir a la página
    page.add(btn_nuevo,btn_consultas)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)