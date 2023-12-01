import flet as ft


def home(page: ft.Page, database_tables: list, tables_data_count: list):
    local_database_tables = [table[0] for table in database_tables]
    local_tables_data_count = [count[0] for count in tables_data_count]
    return [
        ft.AppBar(title=ft.Text("База данных SQLite"), bgcolor=ft.colors.SURFACE_VARIANT),
        *[ft.Card(
            content=ft.Container(
                expand=True,
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM_OUTLINED),
                            title=ft.Text(table),
                            subtitle=ft.Text(
                                f"Таблица имеет записей: {count}."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Показать", on_click=lambda _, tname=table: page.go(f"/table/{tname}")), ft.TextButton("Удалить")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=5),
            )
        ) for table, count in zip(local_database_tables, local_tables_data_count) ],
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=lambda _: page.go("/add-table")),
        ])
    ]
