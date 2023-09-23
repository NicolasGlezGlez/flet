import flet as ft

def main(page: ft.Page):
    
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    
    def minus_click(event):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update() 
        
    
    def plus_click(event):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update() 
        
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE_CIRCLE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD_BOX_ROUNDED, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
# Desktop 
# ft.app(target=main)

# Web App
ft.app(target=main, view=ft.WEB_BROWSER)