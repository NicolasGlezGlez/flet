import flet as ft

async def go_to_store(_):
    await _.page.go_async("/store")
def home_view(page):
    return [
        ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.ElevatedButton("Visit Store", on_click=go_to_store),
        ft.Text("Home"),
    ]