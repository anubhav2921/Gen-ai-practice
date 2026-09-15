import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewStrongPassword_2026!",
    
)

print("Connected:", conn.is_connected())
conn.close()

