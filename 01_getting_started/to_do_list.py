import flet as ft

def main(page: ft.Page):
    def add_text(e):
        if txt_to_do.value != "":
            page.add(ft.Checkbox(label=txt_to_do.value))
            txt_to_do.value = ""
            txt_to_do.focus()
            txt_to_do.update()
        else:
            txt_to_do.focus()
            txt_to_do.update()
    
    txt_to_do = ft.TextField(label="What's needs to be done?")
    
    
    row = ft.Row([
        txt_to_do,
        ft.ElevatedButton(text="Add to do.", on_click=add_text)
        # Pro Mode:
        # ft.ElevatedButton(
        #     text="Add to do.",
        #     on_click=lambda e: (
        #         page.add(ft.Checkbox(label=txt_to_do.value)) if txt_to_do.value != "" else None,
        #         setattr(txt_to_do, 'value', "") if txt_to_do.value != "" else None,
        #         txt_to_do.focus(),
        #         txt_to_do.update()
        #     )[0]
        # )
        
    ])
    page.add(row)

ft.app(target=main)