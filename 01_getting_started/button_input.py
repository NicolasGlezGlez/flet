import flet as ft

def main(page: ft.Page):
    txt_name = ft.TextField(label="Write you're name.")
    lbl_salute = ft.Text()
    
    def salute(e):
        lbl_salute.value = f"Hi, {txt_name.value}!"
        page.update()
        
    row = ft.Row(controls=[
        txt_name,
        ft.ElevatedButton(text="Salute.", on_click=salute),
        lbl_salute
    ])
    page.add(row)
    


ft.app(target=main)