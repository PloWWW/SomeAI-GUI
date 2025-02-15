import flet as ft 

def main(page: ft.Page):
    
    page.title = "Theme light/dark"
    page.theme_mode = 'light'
    
    def change_th(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()    

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.LIGHT_MODE, 
                on_click=change_th)]))

    
ft.app(target = main)