import sqlite3

connection=sqlite3.connect("library_books.db") #( فى ملف اسمه test1 افتحه او لو مش معمول اعملة)

# print(connection.total_changes)
cursor=connection.cursor() #( اعمل بوينتر (مؤشر) يشاور عليه )
# try:
#     cursor.execute("CREATE TABLE fish(name TEXT,spaces TEXT,number INTEGER )") #( اعمل جدول فية الاسم و المساحة نص و الرقم رقم صحيح )
# except:
#     pass
#
# cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
# cursor.execute("INSERT INTO fish VALUES ('Jammy', 'cuttlefish', 7)")
#
# # cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
# # cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
#
# new_name="Jammy"
# raw=cursor.execute("SELECT * FROM fish WHERE name=?",(new_name,),).fetchall() #هات الصف اللي فيه الاسم ده  (jemmy)
# num="shady"
#
# cursor.execute("UPDATE fish SET name = ?  WHERE name = ?",(num,new_name)) # غير ارقم اللي ف الصف ده ل 8
# row=cursor.execute("SELECT name, spaces, number FROM fish").fetchall()
#
#
# cursor.execute("DELETE FROM fish WHERE name = ?", (new_name,))
# cursor.execute("SELECT name, spaces, number FROM fish").fetchall()
#
# name = "memo"
# auther = "a7la"
# rating = 1
#
# cursor.execute(f"INSERT INTO fish VALUES ('{name}', '{auther}', {rating})")
# cursor.execute(f"INSERT INTO library VALUES ('{name}', '{auther}', {rating})")

cursor.execute(
    f"INSERT INTO movie VALUES ('{title}', '{year}', '{description}', '{rating}', '{ranking}', '{review}', '{img_url}')")

rkam=cursor.execute("SELECT title, auther, rating FROM library").fetchall()



print(rkam)




#
# new_tank_number = 2
# moved_fish_name = "Sammy"
# cursor.execute("UPDATE fish SET tank_number = ? WHERE name = ?",(new_tank_number, moved_fish_name))
# row=cursor.execute("SELECT name, spaces, number FROM fish").fetchall()
# print(row)