import sqlite3
import datetime
import io

########################################################
##====================================================##
##~Заполнение sql таблицы, нужно делать в начале года~##
##====================================================##
########################################################

db = sqlite3.connect("base.db")

c = db.cursor()


c.execute(f"""CREATE TABLE IF NOT EXISTS pupils(
    id INTEGER not null  primary key,
    name TEXT,
    class TEXT,

    number_table INTEGER,
    shift INTEGER
)""")#    change INTEGER,

db.commit()
with io.open("basic_information.txt", "r", encoding='utf-8') as f:
    l = f.readlines()
    l = [line.rstrip() for line in l]
    print(l[6])
    u_name = str()
    u_class = str()
    u_table = int()
    u_shift = int()
    for i in range(6, len(l)):
        u_name1, u_name2, u_class, u_number_table, u_shift = map(str, l[i].split())  # и тут тоже добавил
        u_number_table = int(u_number_table)
        u_shift = int(u_shift)
        u_name = f"{u_name1} {u_name2}"
        c.execute(f"INSERT INTO pupils (name, class, number_table, shift) VALUES(?, ?, ?, ?)", (u_name, u_class, u_number_table, u_shift))
        db.commit()



    c.execute("""CREATE TABLE IF NOT EXISTS attendance_log(
        id INTEGER PRIMARY KEY,
        date DATE
    )""")
    db.commit()

    c.execute("""select MAX(id) from pupils""")
    number_of_students = int(c.fetchone()[0])
    for i in range(1, number_of_students + 1):
        c.execute(f"ALTER TABLE attendance_log ADD COLUMN '{i}' BOOL NOT NULL DEFAULT '1'")
    db.commit()


    start = l[1][12:] #"26-07-2022"
    end = l[2][29:] #"5-08-2022"

    d = datetime.datetime.strptime(start, "%d-%m-%Y")
    d = d.date()

    d2 = datetime.datetime.strptime(end, "%d-%m-%Y")
    d2 = d2.date()


    d3 = d2 - d + datetime.timedelta(days=1) # количестро нужных дней
    d3 = str(d3).split()[0]
    print(d3)
    for i in range(int(d3)):
        i = str(d + datetime.timedelta(days = i ))
        print(i)
        print(type(i))
        print(i)
        c.execute(f"INSERT INTO attendance_log (date) VALUES ('{i}')")
    db.commit()
db.close()

