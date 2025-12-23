from database import get_connection

conn = get_connection()
print("DB CONNECTED SUCCESSFULLY")
conn.close()
