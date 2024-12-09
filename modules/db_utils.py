import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mm13113011$",
        database="auto_mate_db"
    )


def save_email_to_db(data):
    try:

        conn = get_db_connection()
        cursor = conn.cursor()


        cursor.execute("""
            INSERT INTO scheduled_emails (sender_email, sender_password, recipient_email, subject, message, scheduled_time, status)
            VALUES (%s, %s, %s, %s, %s, %s, 'pending')
        """, (data["sender_email"], data["sender_password"], data["recipient_email"], data["subject"], data["message"],
              data["scheduled_time"]))

        conn.commit()

        email_id = cursor.lastrowid

        print(f"Scheduled email inserted into database with ID: {email_id}")
        return email_id

    except mysql.connector.Error as err:
        print(f"Error while inserting email into database: {err}")
        raise  # Re-raise the exception for higher-level handling if necessary
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_email_status(email_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE scheduled_emails SET status = %s WHERE id = %s", (status, email_id))
    conn.commit()
    conn.close()

def load_pending_emails():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM scheduled_emails WHERE status = 'pending'")
    emails = cursor.fetchall()

    conn.close()
    return emails
