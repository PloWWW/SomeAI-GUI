import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "Прогнозирование графика"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Переменная для хранения введенных данных
    input_data = None
    # Поле для ввода данных
    input_field = ft.TextField(
        label="Введите данные (что угодно)",
        width=400,
        hint_text="Например: что угодно"
    )
    # Поле для вывода информации
    output_text = ft.Text()
    # Функция, которая будет вызвана при нажатии кнопки
    def button_click(e):
        nonlocal input_data
        # Получаем данные из поля ввода
        input_data = input_field.value
        # Отображаем данные в поле вывода
        output_text.value = f"Введенные данные: {input_data}"
        # Очищаем поле ввода
        input_field.value = ""
        # Обновляем страницу
        page.update()
    # Кнопка для отправки данных
    button = ft.ElevatedButton(
        text="Отправить данные",
        on_click=button_click
    )
    # Панель для вывода с границей и тенью
    output_panel = ft.Container(
        content=ft.Text(f"Плашка для вывода чего-нибудь:", color=ft.colors.WHITE),
        padding=20,
        bgcolor=ft.colors.BLUE,
        border_radius=10,
        width=300,
        alignment=ft.alignment.center,
        border=ft.border.all(2, ft.colors.BLACK),  # Граница
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.BLACK, offset=ft.Offset(5, 5)
        )
    )
    def button_click(e):
        output_text.value = "Текст обновлен!"
        page.update()
    # Создаем кнопку
    button2 = ft.ElevatedButton(
        text="Обновить текст",
        on_click=button_click
    )
    # Используем Stack для точного позиционирования
    stack = ft.Stack(
        [
            # Поле ввода с координатами (x=50, y=100)
            ft.Container(
                content=input_field,
                top=300,  # Отступ сверху
                left=100,   # Отступ слева
            ),
            # Кнопка с координатами (x=50, y=150)
            ft.Container(
                content=button,
                top=360,  # Отступ сверху
                left=100,   # Отступ слева
            ),
            # Поле вывода с координатами (x=50, y=200)
            ft.Container(
                content=output_text,
                top=320,  # Отступ сверху
                left=500,   # Отступ слева
            ),
            # Панель с границей и тенью (x=50, y=400)
            ft.Container(
                content=output_panel,
                top=295,  # Отступ сверху
                left=700,   # Отступ слева
            ),
            ft.Container(
                content=button2,
                top=370,  # Отступ сверху
                left=700,   # Отступ слева
            ),
        ],
        width=page.width,  # Ширина Stack равна ширине страницы
        height=page.height  # Высота Stack равна высоте страницы
    )
    # Добавляем Stack на страницу
    page.add(stack)

# Запускаем приложение
ft.app(target=main)
