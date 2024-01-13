import flet as ft
from sql_query import *
import sqlite3 as sql


def add_table_data(page: ft.Page, db: sql.Connection, name_id: str):
    tables, table_headers = show_table(db=db, table_name=name_id)
    
    def add_new_datarows(e):
        headers = table_headers[1:]
        body = []
        empty_textfield = False
        for data_row in add_data_table_ref.current.rows:
            row_data = []
            for data_cell in data_row.cells:
                text_value = data_cell.content.value
                if text_value == "":
                    empty_textfield = True
                    break
                row_data.append(text_value)
            body.append(row_data)
        if not empty_textfield:
            data = [
                {f"'{headers[i]}'":row[i] for i in range(len(row))}
                for row in body
            ]
            for data_row in data:
                update_table(db, name_id, data_row)
                page.go("/")
    
    def check_column_type(item):
        if type(item) is int:
            return ft.KeyboardType.NUMBER
        return ft.KeyboardType.TEXT
    
    def change_add_data_count(e):
        add_data_table_ref.current.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.TextField(
                        text_size=14,
                        border=ft.InputBorder.NONE,
                        keyboard_type=check_column_type(item))
                    ) for item in (tables[0][1:] if len(tables) > 0 else table_headers[1:])
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
                        ) for head in table_headers[1:]
                    ],
                    vertical_lines=ft.BorderSide(1, ft.colors.GREY),
                    data_row_min_height=70,
                    column_spacing=20,
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.TextField(
                                    text_size=13,
                                    border=ft.InputBorder.NONE,
                                    keyboard_type=check_column_type(item))
                                ) for item in (tables[0][1:] if len(tables) > 0 else table_headers[1:])
                            ],
                        )
                    ],
                ),
        ]),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            controls=[
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=change_add_data_count),
            ft.ElevatedButton("Сохранить", on_click=add_new_datarows),
        ])
    ]