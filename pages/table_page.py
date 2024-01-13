import flet as ft
import csv
import os
from sql_query import *
import sqlite3 as sql

def table(page: ft.Page, db: sql.Connection, name_id: str):
    tables, table_headers = show_table(db=db, table_name=name_id)
    
    def save_to_file(tname, extension):
        internal_storage_path = os.path.join(os.getcwd(), f"{tname}.{extension}")
        external_storage_path = os.path.join('/sdcard', f"{tname}.{extension}")
        if tname == "csv":
            try:
                with open(internal_storage_path, "w", encoding="utf-8") as file:
                    writer = csv.writer(file, delimiter=';', lineterminator='\n')
                    writer.writerow(table_headers)
                    for row in tables: 
                        writer.writerow(row)
            except Exception as error:
                print(error)
    
    return [
        ft.AppBar(title=ft.Text("База данных SQLite"), bgcolor=ft.colors.SURFACE_VARIANT, ),
        ft.DataTable(
            expand=True,
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
        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
            ft.Row(controls=[
                ft.ElevatedButton("CSV", on_click=lambda _: save_to_file(name_id, "csv")),
                ft.ElevatedButton("Excel", on_click=lambda _: save_to_file(name_id, "excel")),
                ft.ElevatedButton("PDF", on_click=lambda _: save_to_file(name_id, "pdf")),
                ft.ElevatedButton("Docx", on_click=lambda _: save_to_file(name_id, "docx")),
            ]),
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=lambda _: page.go(f"/table/{name_id}/add-table-data")),
        ])
    ]