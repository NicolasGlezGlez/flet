import flet as ft

def main(page: ft.Page):
    data_to_show = ["Python", "Flet", "Flutter"]
    labels = []
    
    for i in data_to_show:
        labels.append(ft.Text(i))
    
    row_data = ft.Row(controls=labels)
    page.add(row_data)
    
ft.app(target=main)