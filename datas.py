import sqlite3

db = sqlite3.connect('dsdd.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dfs_users(
               id INTEGER,
               name TEXT,
               phone_num TEXT,
               adres TEXT)
''')
db.commit()

async def save_users(id,name,phone_numbeer,adddres):
    cursor.execute('''
INSERT INTO dfs_users(
                   id,name,phone_num,adres)
                   VALUES(?,?,?,?)
''',(id,name,phone_numbeer,adddres))
    db.commit()



async def show_users():
    cursor.execute('SELECT * FROM dfs_users')
    datas = cursor.fetchall()
    return datas

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS admins(
#                 id INTEGER)
# '''
# )
# db.commit()
# async def save_admins(id):
#     cursor.execute('''
# INSERT INTO dfs_users(
#                    id)
#                    VALUES(?)
# ''',(id))
#     db.commit()

# async def show_admins():
#     cursor.execute('SELECT * FROM admins')
#     datas = cursor.fetchall
#     return datas