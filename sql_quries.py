from sql_connector import make_connection
from faker import Faker

conn = make_connection()
cursor = conn.cursor()

def create_tables() -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
        )""")
    conn.commit()

def add_user(name, email, password) -> None:
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()

def get_user(email) -> None:
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    print(cursor.fetchall())

def get_all_users() -> None:
    cursor.execute("SELECT * FROM users")
    return {"users": cursor.fetchall()}

if __name__ == "__main__":
    create_tables()
    for _ in range(10):
        fake = Faker()
        add_user(fake.name(), fake.email(), fake.password())