import flet as ft
from pages.home_view import home_view
from pages.store_view import store_view

async def main(page: ft.Page):
    page.title = "Routes Example"

    async def go_to_store(_):
        await page.go_async("/store")
    async def go_to_home(_):
        await page.go_async("/")
        
    async def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    home_view(page)
                    # [
                    #     ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    #     ft.ElevatedButton("Visit Store", on_click=go_to_store),
                    #     ft.Text("Home"),
                    # ],
                )
            )
        elif page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    store_view(page)
                    # [
                    #     ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                    #     ft.ElevatedButton("Go Home", on_click=go_to_home),
                    #     ft.Text("Store"),
                    # ],
                )
            )
        await page.update_async()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go_async(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    await page.go_async(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)