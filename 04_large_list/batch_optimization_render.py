import flet as ft

def main(page: ft.Page):
    list_view = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(list_view)
    
    for i in range(5100):
        list_view.controls.append(ft.Text(f"Line {i}"))
        
        if i % 500 == 0:
            page.update()
    page.update()
    
ft.app(target=main)
    
    