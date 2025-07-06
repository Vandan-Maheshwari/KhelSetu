import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kinshu2006',  # replace with your actual MySQL password
            database='khelsetu'
        )
        if conn.is_connected():
            print("✅ Connected to KhelSetu Database")
            return conn
    except Error as e:
        print("❌ Error while connecting to MySQL", e)
        return None

def register_user():
    print("\n===== KHEL SETU: Player Registration =====")

    name = input("Full Name: ")
    age = int(input("Age: "))
    gender = input("Gender (Male/Female/Other): ")
    sport = input("Sport interested in: ")
    state = input("State: ")
    district = input("District: ")
    phone = input("Phone Number: ")
    email = input("Email ID: ")

    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO users
                (full_name, age, gender, sport, state, district, phone_number, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (name, age, gender, sport, state, district, phone, email)
            cursor.execute(query, values)
            conn.commit()
            print("🎉 User Registered Successfully with ID:", cursor.lastrowid)
        except Error as e:
            print("❌ Failed to insert data:", e)
        finally:
            cursor.close()
            conn.close()

# Run the function
register_user()
