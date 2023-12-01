import flet as ft


def add_table(page: ft.Page):
    
    def add_row_table(e):
        table_column.current.controls.append(
            ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.START,
                controls=[
                        ft.TextField(label="Название столбца", width=550),
                        ft.Dropdown(label="Тип данных", options=data_type_opstions),
                        ft.Checkbox(label="Пустой", height=50, value=False),
                ]
            )
        )
        
        table_column.current.update()
    
    def add_new_table(e):
        
        page.go("/")
    
    data_type_opstions = [
        ft.dropdown.Option(
            text
        ) for text in ["NULL", "INTEGER", "REAL", "TEXT", "BLOB"]
    ]
    
    table_name_ref = ft.Ref[ft.TextField]()
    
    table_column = ft.Ref[ft.Column]()
    
    return [
        ft.AppBar(title=ft.Text("Добавить новую таблицу"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.TextField(label="Название таблицы", icon=ft.icons.ALBUM_OUTLINED, ref=table_name_ref),
        ft.Row(
            expand=True,
            wrap=True,
            scroll=ft.ScrollMode.ALWAYS,
            vertical_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.START,
            controls=[        
                ft.Column(
                    ref=table_column,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                    ft.TextField(label="Название столбца", width=550),
                                    ft.Dropdown(label="Тип данных", options=data_type_opstions),
                                    ft.Checkbox(label="Пустой", height=50, value=False),
                            ]
                        )
                    ]  
                ),
            ]
        ),
        ft.Row(width=page.window_width, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=add_row_table),
            ft.ElevatedButton("Добавить", on_click=add_new_table),
        ])
    ]