import flet as ft

async def go_to_home(_):
    await _.page.go_async("/")
    
def store_view(page):
    return [
        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.ElevatedButton("Go Home", on_click=go_to_home),
        ft.Text("Store"),
    ]