import flet as ft
from sql_query import *
from pages import ( add_table_data_page, add_table_page, home_page, table_page )


db_file = "database.db"
db = create_connection(db_file)


tables, table_headers = show_table(db=db, table_name="user")

database_tables, tables_data_count = show_tables(db)



def main(page: ft.Page):
    page.title = "SQLite to file"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_center()
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    
    
    def route_change(route):
        troute = ft.TemplateRoute(page.route)
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                home_page.home(page, database_tables, tables_data_count),
            )
        )
        if troute.match("/table/:name_id"):
            name_id = troute.name_id
            page.go(f"/table/{name_id}")
            tables, table_headers = show_table(db=db, table_name=name_id)
            if page.route == f"/table/{name_id}":
                page.views.append(
                    ft.View(
                        f"/table/{name_id}",
                        table_page.table(page, tables, table_headers, name_id),
                    )
                )
        if troute.match("/table/:name_id/add-table-data"):
            name_id = troute.name_id
            if page.route == f"/table/{name_id}/add-table-data":
                page.views.append(
                    ft.View(
                        f"/table/{name_id}/add-table-data",
                        add_table_data_page.add_table_data(page, tables, table_headers),
                    )
                )
        if page.route == "/add-table":
            page.views.append(
                ft.View(
                    "/add-table",
                    add_table_page.add_table(page),
                )
            )
        page.update()

        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main)

db.close()