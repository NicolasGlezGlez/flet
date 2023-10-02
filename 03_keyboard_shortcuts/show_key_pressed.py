import flet as ft

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key:
            if e.shift:
                page.add(ft.Text(f"Key pressed: Shift + {e.key}"))
            elif e.ctrl:
                page.add(ft.Text(f"Key pressed: Ctrl + {e.key}"))
            elif e.alt:
                page.add(ft.Text(f"Key pressed: Alt + {e.key}"))
            elif e.meta:
                page.add(ft.Text(f"Key pressed: Meta + {e.key}"))
            else:
                page.add(ft.Text(f"Another key was pressed."))
        
    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with CTRL, SHIFT, ALT and Meta keys")
    )
    
ft.app(target=main)
    