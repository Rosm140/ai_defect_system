import sqlite3
import csv
from datetime import datetime
import os

db_path = "logs/inspection.db"
csv_path = "logs/results.csv"


def log_result(product_name, predicted_class, confidence,
               image_path="", sensor_trigger="YES",
               action_taken="PASS", defect_type="", remarks=""):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # SQLite insert
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO inspection_results (
        timestamp,
        product_name,
        predicted_class,
        confidence,
        image_path,
        sensor_trigger,
        action_taken,
        defect_type,
        remarks
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        product_name,
        predicted_class,
        confidence,
        image_path,
        sensor_trigger,
        action_taken,
        defect_type,
        remarks
    ))

    conn.commit()
    conn.close()

    # CSV insert
    file_exists = os.path.isfile(csv_path)

    with open(csv_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "product_name",
                "predicted_class",
                "confidence",
                "image_path",
                "sensor_trigger",
                "action_taken",
                "defect_type",
                "remarks"
            ])

        writer.writerow([
            timestamp,
            product_name,
            predicted_class,
            confidence,
            image_path,
            sensor_trigger,
            action_taken,
            defect_type,
            remarks
        ])

    print("Result logged successfully")