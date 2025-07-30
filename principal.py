import flet as ft
#import registro_biomasa as registro
#import consulta_usuario as cu

def main(page: ft.Page):

    #def mostrar_registro(e: ft.ControlEvent):
        #page.clean()
        #registro.main(page)

    #def mostrar_consulta(e: ft.ControlEvent):
        #page.clean()
        #cu.main(page)

    #Configuración de la página
    page.title = "Menú principal"
    page.theme_mode= "light"
    page.appbar = ft.AppBar(
        title= ft.Text("Sistema de Gestión de Bioenergías"),
        leading= ft.Icon("energy_savings_leaf"),
        color= "white",
        bgcolor= "purple",  
    )

    #Componentes de la página
    
    btn_registro = ft.ElevatedButton("Registro")
    btn_consultas = ft.ElevatedButton("Consulta")
    #Añadir a la página
    page.add(btn_registro,btn_consultas)
    page.update()
if __name__ == "__main__":
    ft.app(target=main)