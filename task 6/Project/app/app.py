from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST")
        )
        return "Database Connected Successfully!"
    except:
        return "Database Connection Failed!"

@app.route('/')
def home():
    return connect_db()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
