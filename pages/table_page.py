import flet as ft
from sql_query import *
import sqlite3 as sql

def table(page: ft.Page, db: sql.Connection, name_id: str):
    tables, table_headers = show_table(db=db, table_name=name_id)
    
    return [
        ft.AppBar(title=ft.Text("База данных SQLite"), bgcolor=ft.colors.SURFACE_VARIANT, ),
        ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Text(head.title())
                ) for head in table_headers
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item))
                        for item in data
                    ],
                ) for data in tables
            ],
        ),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=lambda _: page.go(f"/table/{name_id}/add-table-data")),
        ])
    ]