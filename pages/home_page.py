import flet as ft
import sqlite3 as sql
from sql_query import *
import csv


def home(page: ft.Page, db: sql.Connection):
    database_tables, tables_data_count = show_tables(db)
    
    local_database_tables = [table[0] for table in database_tables]
    local_tables_data_count = [count[0] for count in tables_data_count]
    tables, table_headers = None, None
    
    def save_to_file(tname):
        file_picker_dialog.save_file(
            file_name=tname.capitalize(),
            allowed_extensions=["csv", "xlsx", "pdf", "docx"],
            file_type=ft.FilePickerFileType.CUSTOM
        )
        nonlocal tables
        nonlocal table_headers
        tables, table_headers = show_table(db=db, table_name=tname)
    
    def save_file_result(e: ft.FilePickerResultEvent):
        save_path = e.path
        if save_path:
            try:
                with open(save_path, "w", encoding="utf-8") as file:
                    writer = csv.writer(file, delimiter=';', lineterminator='\n')
                    writer.writerow(table_headers)
                    for row in tables: 
                        writer.writerow(row)
            except Exception as error:
                print(error)
    
    file_picker_dialog = ft.FilePicker(on_result=save_file_result)
    
    page.overlay.append(file_picker_dialog)
    page.update()
    
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
                            [
                                ft.TextButton("Сохранить", on_click=lambda _, tname=table: save_to_file(tname)),
                                ft.TextButton("Показать", on_click=lambda _, tname=table: page.go(f"/table/{tname}")), 
                                ft.TextButton("Удалить")
                                ],
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
