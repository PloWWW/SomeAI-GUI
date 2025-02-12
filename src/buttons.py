import flet as ft 
import flet_material as fm

def main(page: ft.Page):

    def click(e):
        print("button clicked")
        
    page.bgcolor = fm.Theme.bgcolor
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    button = fm.Buttons(width=220, height=55, title="Give this repo a star!",on_click = click)
    page.add(button)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)