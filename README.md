 VitaBand - AI-Powered Stress Detection Wristband

📌 Project Overview

VitaBand is an AI-powered, low-cost stress-detection wristband designed to help individuals track their stress levels and take action before stress becomes overwhelming. Using biometric sensors and an ESP32 microcontroller, VitaBand collects stress-related data and transmits it securely to a Python-based mobile application. This project was created for the 2024-2025 Youth Innovation Competition by the Aga Khan Foundation (AKF) and follows the competition's theme, "Inspiring Hope, Changing Lives."

🔍 Problem Statement

Stress and anxiety levels among students and young individuals are at an all-time high, yet mental health tools remain inaccessible, expensive, and dependent on smartphones or the internet. Many existing solutions focus on treatment rather than early detection and prevention. VitaBand aims to bridge this gap by providing a low-cost, screen-free, and offline-friendly solution that helps individuals detect and manage stress in real-time.

🎯 Competition & Submission Details

Event: 2024-2025 Youth Innovation Competition

Hosted by: Aga Khan Foundation (AKF)

Deadline: March 3rd, 2025

Final Presentation: On-site in Dallas, Spring 2025

Judging Criteria:

Originality – Unique approach to solving a real-world issue

Impact – How it benefits the community

Feasibility – How realistic and implementable it is

Sustainability – Long-term effectiveness and scalability

Presentation Quality – Clarity and effectiveness of the final video/slideshow

Awards:

🏆 1st Place: $500

🥈 2nd Place: $300

🥉 3rd Place: $200

🌟 What Makes VitaBand Unique?

✅ Low-Cost & Accessible

Uses ESP32 microcontroller (affordable and widely available)

No screen or expensive hardware – keeps manufacturing costs low

No WiFi/Bluetooth dependency – works offline

✅ Real-Time Stress Detection

Uses Heart Rate Variability (HRV), Electrodermal Activity (EDA), and Skin Temperature

Detects stress levels and triggers LED indicators to alert users

Sends encrypted data to the mobile app for analysis

✅ Mental Health Interventions

Guides users through breathing exercises & mindfulness techniques when stress is detected

Logs stress trends in an app (like iPhone Screen Time but for mental health)

Suggests interventions before stress escalates to a critical level

✅ Privacy-First Approach

Local data storage – no cloud storage or third-party tracking

End-to-end encryption for all biometric data

User data is not shared without explicit consent

🛠️ How VitaBand Works

📡 Hardware & Sensors

ESP32-WROOM-32 – Microcontroller for handling sensors and Bluetooth communication

HRV Sensor (MAX30102) – Measures heart rate variability

EDA Sensor (GSR Sensor) – Tracks sweat levels

Skin Temperature Sensor (MLX90614) – Measures stress-related temperature fluctuations

LED Indicator – Lights up when stress is detected

USB-C Charging Port – For easy charging

3D-Printed Wristband – Lightweight, comfortable, and customizable

📲 Mobile App Features (Python-Based)

Dashboard – Shows real-time stress indicators

Historical Trends – Graphs with line of best fit to display stress patterns

User Mood Tracking – Occasionally asks users to self-report their mood

GAD-7 Anxiety Screening – Conducts a clinically recognized baseline anxiety test

Encrypted Data Transmission – Ensures biometric data remains private

💾 Project Structure

VitaBand/
│── firmware/                  # ESP32 Firmware Code
│   ├── firmware.ino            # Main Microcontroller Code
│── app/                        # Python-Based App
│   ├── app.py                  # Flask API & Database Handling
│   ├── database.sqlite         # Stores Stress & Mood Logs
│   ├── visualization.py        # Graph & Data Analysis
│── 3d_designs/                  # 3D Print Files for Wristband
│   ├── vitaband_v1.stl         # 3D Model File
│── docs/                        # Documentation & Instructions
│   ├── README.md               # This File
│   ├── VitaBand_Project.pdf    # Full Technical Document
│── requirements.txt            # Python Dependencies
│── main.py                     # Entry Script
│── .gitignore                   # Ignore Unnecessary Files

📝 Pseudocode: How Everything Works

# ESP32 Microcontroller - Sensor Processing & Bluetooth Transmission
Initialize ESP32 microcontroller
Initialize HRV, EDA, and Temperature sensors
Initialize LED Indicator
Initialize Bluetooth module

While device is ON:
    Read HRV, EDA, and Temperature sensor data
    If (HRV < Threshold) AND (EDA > Threshold) AND (Temp > Threshold):
        Set stress_detected = True
        Turn ON LED Indicator
    Else:
        Set stress_detected = False
        Turn OFF LED Indicator
    Encrypt and transmit data to the app via Bluetooth

# Flask API - Backend Data Handling
Initialize Flask app
Initialize SQLite database

Define "/stress" endpoint:
    Receive encrypted HRV, EDA, Temperature data
    Store data in SQLite database
    Return "Data received securely"

# Mobile App UI - Data Visualization
Create Dashboard:
    - Live stress indicator
    - Historical stress trend visualization
    - Personalized intervention notifications

Function ask_user_mood():
    Prompt user for mood check-in every 3 hours
    Store self-reported data for correlation analysis

While App is running:
    Display real-time stress updates
    Log trends & generate insights

🚀 How to Set Up the Project

🔹 1. Clone Repository

git clone https://github.com/YOUR-USERNAME/VitaBand.git
cd VitaBand

🔹 2. Install Dependencies

pip install -r requirements.txt

🔹 3. Run Flask API

python app.py

🔹 4. Connect ESP32

Upload firmware.ino to your ESP32 using Arduino IDE

Pair with the mobile app via Bluetooth

📌 Next Steps

1️⃣ Test ESP32 sensor integration & LED activation 2️⃣ Deploy Flask API & connect with Replit/GitHub Actions 3️⃣ Finalize app UI & stress visualization 4️⃣ Optimize wristband 3D design 5️⃣ Submit final project video & slideshow

📌 Want to contribute? Fork this repo & submit a pull request! 🚀

