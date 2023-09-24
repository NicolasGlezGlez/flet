import flet as ft

def main(page: ft.Page):
    txt_name = ft.TextField(label="Write you're name.")
    def salute(e):
        print (f"Hi, {txt_name.value}!")
    row = ft.Row(controls=[
        txt_name,
        ft.ElevatedButton(text="Salute.", on_click=salute)
    ])
    page.add(row)
    


ft.app(target=main)