import sqlite3 as sql
from sqlite3 import Error



def create_connection(db_file: str):
    db = None
    try:
        db = sql.connect(db_file, check_same_thread=False)
    except Error as e:
        print(e)

    return db

def create_table(db: sql.Connection, table_name: str, table_values: dict):
    
    cursor = db.cursor()
    
    sql_query = ""
    for key, item in table_values.items():
        sql_query += f"'{key}' {item},\n\t"
        
    sql_query = sql_query.rstrip(",\n\t")
    
    sql_query_all = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        {sql_query}
    )"""

    cursor.execute(sql_query_all)
    
    db.commit()
    
    return cursor.lastrowid

def show_tables(db: sql.Connection):
    cursor = db.cursor()
    
    cursor.execute("""SELECT name FROM sqlite_master  
        WHERE type='table';""")

    res = cursor.fetchall()
    res_count = []
    
    for name in res:  
        cursor.execute(f"""
            SELECT COUNT(*) FROM {name[0]}
        """)
        count = cursor.fetchall()
        res_count.append(*count)
    
    return res, res_count


def show_table(db: sql.Connection, table_name: str):
    cursor = db.cursor()
    
    sql_query = f"SELECT * FROM {table_name}"
    cursor.execute(sql_query)
    
    response = cursor.fetchall()
    headers = list(map(lambda x: x[0], cursor.description))
    data = []
    if not len(response):
        return data, headers
    
    for res in response:
        data.append(res)
    return data, headers

def update_table(db: sql.Connection, table_name: str, table_values: dict):
    cursor = db.cursor()
    
    table_columns =  ", ".join(table_values.keys())
    table_columns_values = ", ".join(["?" for _ in table_values.values()])
    cursor.execute(f"""
        INSERT INTO {table_name} ({table_columns}) VALUES ({table_columns_values})
    """, tuple(table_values.values()))
    
    db.commit()
    
    return cursor.lastrowid


def delete_table(db: sql.Connection, table_name: str,):
    cursor = db.cursor()
    
    cursor.execute(f"""
        DROP TABLE IF EXISTS {table_name};
    """)
    
    db.commit()
    
    return cursor.lastrowid
    