import flet as ft

def main(page: ft.Page):

    grid_view = ft.GridView(expand=True, max_extent=100, child_aspect_ratio=1)
    page.add(grid_view)
    
    for i in range(5000):
        grid_view.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()
    
ft.app(target=main)