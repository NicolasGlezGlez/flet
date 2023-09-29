import flet as ft

def main(page: ft.Page):
    lbl_text = ft.Text(value="Hello, world!", size=20, color="red", bgcolor="yellow", weight="bold", italic=True)
    
    page.add(lbl_text)
    
ft.app(target=main)