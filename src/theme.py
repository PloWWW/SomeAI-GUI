import flet as ft 

def main(page: ft.Page):
    
    page.title = "Theme light/dark"
    page.theme_mode = 'light'
    
    def change_th(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()     

    def toggle_icon(e):
        if page.theme_mode == 'light':
            ft.IconButton(
            icon = ft.icons.LIGHT_MODE,
            on_click=change_th)
            page.update()
        else:
            ft.IconButton(
            icon = ft.icons.DARK_MODE,
            on_click=change_th)
            page.update()

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.DARK_MODE, 
                on_click=change_th)]))

    
ft.app(target = main)