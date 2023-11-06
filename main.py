import flet as ft

async def main(page: ft.Page):
    page.title = "Routes Example"

    async def go_to_store(_):
        await page.go_async("/store")
    async def go_to_home(_):
        await page.go_async("/")
        
    async def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=go_to_store),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=go_to_home),
                        ft.Text("Store"),
                    ],
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