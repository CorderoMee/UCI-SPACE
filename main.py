import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "App Hola Mundo"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    # Texto grande centrado
    titulo = ft.Text("Hola Mundo", size=40, weight="bold")
    
    # Botón
    btn = ft.ElevatedButton("Saludar", width=200)
    
    # Función que se ejecuta al presionar el botón
    def saludar(e):
        page.add(ft.Text("olaaaaaa", size=20, color="blue"))
    
    btn.on_click = saludar
    
    # Añadir elementos a la página
    page.add(titulo, btn)

# Ejecutar la app (modo escritorio por defecto)
ft.app(target=main, view=ft.WEB_BROWSER)
