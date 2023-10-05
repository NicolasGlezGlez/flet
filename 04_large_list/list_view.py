import flet as ft

def main(page: ft.Page):
    list_view = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        list_view.controls.append(ft.Text(f"Line {i}"))
    page.add(list_view)
    
ft.app(target=main)