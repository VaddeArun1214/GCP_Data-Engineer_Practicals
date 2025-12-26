import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = conn.cursor()
cursor.execute("SELECT NOW();")
result = cursor.fetchone()

print("Connected Successfully", result)

# cursor.execute("""
# INSERT INTO customers (name, email) VALUES
# ('John Doe', 'johndoe@example.com'),
# ('Jane Smith', 'janesmith@example.com');
#                """)

# conn.commit()

cursor.execute("SELECT * FROM employees;")
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()
