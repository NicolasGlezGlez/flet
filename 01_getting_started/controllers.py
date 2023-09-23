import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.add(t) # shortcut of page.controls.append(t)
    page.update()
    
    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)
        

ft.app(target=main)