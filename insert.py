import mysql.connector

conn = mysql.connector.connect(
     host="localhost",
    user="root",
    password="prekshajain26",
    database="myproject"  
)
x=conn.cursor()
'''s1="insert into suppliers(supplierID,supplierName,contact) values(%s,%s,%s)"
svalues=[("S102","rahul","8056278670"),("S103","reeta","7152278670")]
x.executemany(s1,svalues)'''
c1="insert into category(categoryID,categoryName)values(%s,%s)"
cvalues=[("C101","Grocery")]
x.executemany(c1,cvalues)
conn.commit()
print("record inserted")

x.close()
