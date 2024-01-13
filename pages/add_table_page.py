import flet as ft
import sqlite3 as sql
from sql_query import *

def add_table(page: ft.Page, db: sql.Connection):
    
    def add_row_table(e):
        table_column.current.controls.append(
            ft.Column(
                controls=[
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                                ft.TextField(label="Название столбца", expand=True),
                        ]
                    ),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                                ft.Dropdown(label="Тип данных", options=data_type_opstions, expand=True),
                                ft.Checkbox(label="ПУСТОЙ", value=False, expand=True),
                        ]
                    )
                ]
            )
        )
        
        table_column.current.update()
    
    def add_new_table(e):
        table_name = table_name_ref.current.value.lower()
        print(table_name)
        table_values = { }
        for column in table_column.current.controls:
            data_params = []
            for row in column.controls:
                for item in row.controls:
                    data_params.append(item.value)
            table_values.update({data_params[0].lower(): f"{data_params[1]} {"" if data_params[2] else "NOT"} NULL" })
        create_table(db, table_name, table_values)
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
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    controls=[
                                            ft.TextField(label="Название столбца", expand=True),
                                    ]
                                ),
                                ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                            ft.Dropdown(label="Тип данных", options=data_type_opstions, expand=True),
                                            ft.Checkbox(label="ПУСТОЙ", value=False, expand=True),
                                    ]
                                )
                            ]
                        )
                    ]  
                ),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            controls=[
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=add_row_table),
            ft.ElevatedButton("Добавить", on_click=add_new_table),
        ])
    ]