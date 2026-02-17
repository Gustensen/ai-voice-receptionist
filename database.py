import os
import sqlite3

# Define the path ONCE at the top
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "leads.db") # Stick to 'leads.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            service TEXT,
            price INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database initialized at: {db_path}")

def save_lead(name, phone, service, price):
    # Use the global db_path defined at the top
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leads (name, phone, service, price)
        VALUES (?, ?, ?, ?)
    ''', (name, phone, service, price))
    conn.commit()
    conn.close()
    print(f"Lead Saved: {name} - {service}")

if __name__ == "__main__":
    init_db()