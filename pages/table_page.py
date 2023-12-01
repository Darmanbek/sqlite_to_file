import flet as ft

def table(page: ft.Page, tables: list, table_headers: list, name_id: str):
    
    return [
        ft.AppBar(title=ft.Text("База данных SQLite"), bgcolor=ft.colors.SURFACE_VARIANT),
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
            ft.IconButton(icon=ft.icons.ADD, icon_size=35, on_click=lambda _: page.go(f"/table{name_id}/add-table-data")),
        ])
    ]