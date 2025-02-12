import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt

def main(page):
    page.title = "SomeAI GUI"
    content = ft.Column(expand=True)  
    page.window_width = 500
    page.window_height = 500

    def update_content(e):
        selected_value = dropdown.value
        content.controls.clear()

        if selected_value == "График":
            fig, ax = plt.subplots(figsize=(5, 4))
            fruits = ["apple", "blueberry", "cherry", "orange"]
            counts = [40, 100, 190, 55]
            bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

            ax.bar(fruits, counts, color=bar_colors)
            ax.set_ylabel("fruit supply")
            ax.set_title("Fruit supply by kind and color")

            chart = MatplotlibChart(fig)
            content.controls.append(chart)

        elif selected_value == "Кнопка":
            button = ft.TextButton(text="Нажми меня!", on_click=lambda e: print("Кнопка нажата!"))
            content.controls.append(button)

        elif selected_value == "Картинка":
            image = ft.Image(src="https://i.pinimg.com/736x/b7/b7/b4/b7b7b44c7106c5e6bb532f9e24cf38b6.jpg")
            content.controls.append(image)

        content.update()

    dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("График"),
            ft.dropdown.Option("Кнопка"),
            ft.dropdown.Option("Картинка"),
        ],
        label="Выберите элемент для отображения",
        on_change=update_content,
    )

    page.add(
        ft.Column([
            dropdown, 
            content    
        ], expand=True) 
    )

ft.app(target=main)
