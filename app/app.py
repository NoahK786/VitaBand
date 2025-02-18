from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stress_data (
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                 HRV INT, EDA INT, Temp INT, Stress_Level TEXT)''')
    conn.commit()
    conn.close()

@app.route('/stress', methods=['POST'])
def receive_data():
    data = request.json
    HRV, EDA, Temp = data["HRV"], data["EDA"], data["Temp"]
    stress_level = "High" if (HRV < 50 and EDA > 300 and Temp > 90) else "Normal"
    
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    c.execute("INSERT INTO stress_data (HRV, EDA, Temp, Stress_Level) VALUES (?, ?, ?, ?)", 
              (HRV, EDA, Temp, stress_level))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "Data Stored", "Stress_Level": stress_level})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
