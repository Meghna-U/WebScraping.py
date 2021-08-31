import sqlite3
def connect(dbname):
    c=sqlite3.connect(dbname)
    c.execute("CREATE A TABLE IF IT DOES NOT EXIST OYO_HOTELS (NAME TEXT,ADDRESS TEXT,PRICE INT,AMENITIES TEXT,RATING TEXT)")
    print("Table has been created successfully")
    c.close()
def insert_in_table(dbname,values):
    c=sqlite3.connect(dbname)
    print("Information inserted into table: "+str(values))
    insert_in_sql="INSERT IN OYO_HOTELS (NAME,ADDRESS,PRICE,AMENITIES,RATING) VALUES (?,?,?,?,?)"
    c.execute(insert_in_sql,values)
    c.commit()
    c.close()
def retrieve_hotelinfo(dbname):
    c=sqlite3.connect(dbname)
    cr=c.cursor()
    cr.execute("SELECT * FROM OYO_HOTELS")
    tableof_data=cr.fetchall()
    for each_record in tableof_data:
        print(each_record)
