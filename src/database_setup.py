import sqlite3

# Database path
db_path = "logs/inspection.db"

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Create cursor
cursor = conn.cursor()

# Create main table
cursor.execute("""
CREATE TABLE IF NOT EXISTS inspection_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    product_name TEXT NOT NULL,
    predicted_class TEXT NOT NULL,
    confidence REAL NOT NULL,
    image_path TEXT,
    sensor_trigger TEXT,
    action_taken TEXT,
    defect_type TEXT,
    remarks TEXT
)
""")

# Save and close
conn.commit()
conn.close()

print("Database and table created successfully")