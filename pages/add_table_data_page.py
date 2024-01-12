import flet as ft
from sql_query import *
import sqlite3 as sql


def add_table_data(page: ft.Page, db: sql.Connection, name_id: str):
    tables, table_headers = show_table(db=db, table_name=name_id)
    
    def add_new_datarows():
        pass
    
    def check_column_type(item):
        if type(item) is int:
            return ft.KeyboardType.NUMBER
        return ft.KeyboardType.TEXT
    
    def change_add_data_count(e):
        add_data_table_ref.current.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.TextField(
                        height=50,
                        keyboard_type=check_column_type(item))
                    ) for item in tables[0]
                ],
            )
        )
        add_data_table_ref.current.update()

    add_data_table_ref = ft.Ref[ft.DataTable]()
    
    return [
        ft.AppBar(title=ft.Text("Добавить новую запись"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.Row(
        wrap=True,
        expand=True,
        scroll="always",
        controls=[
            ft.DataTable(
                width=page.window_width,
                ref=add_data_table_ref,
                columns=[
                    ft.DataColumn(
                        ft.Text(head.title())
                    ) for head in table_headers
                ],
                vertical_lines=ft.BorderSide(1, ft.colors.GREY),
                data_row_min_height=70,
                data_row_max_height=70,
                column_spacing=20,
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.TextField(
                                height=50,
                                keyboard_type=check_column_type(item))
                            ) for item in tables[0]
                        ],
                    )
                ],
            ),
            ]),
        ft.Row(width=page.window_width, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=change_add_data_count),
            ft.ElevatedButton("Сохранить", on_click=lambda _: page.go("/")),
        ])
    ]