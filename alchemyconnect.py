from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import text
host="localhost"
user="root"
password="prekshajain26"
database="myproject"
port=3306  
database_url=create_engine("mysql+pymysql://root:prekshajain26@localhost:3306/myproject")
print (database_url)
conn=database_url.connect()
sql_query=pd.read_sql_query('select * from myproject.suppliers,myproject.category',conn)
df=pd.DataFrame(sql_query)
print(df)
conn.close