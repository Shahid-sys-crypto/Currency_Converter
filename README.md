# 💱 Currency Converter (Python + Tkinter + JSON)

A simple desktop **Currency Converter** application built using **Python**, **Tkinter**, and **JSON** for storing exchange rates.

This application allows users to:
- 💰 Enter an amount
- 🌍 Choose source currency
- 🔄 Convert to another currency
- 📂 Load exchange rates from a JSON file

---

## 🚀 Features

- Simple and clean GUI
- JSON-based exchange rate storage
- Real-time conversion inside the app
- Error handling for invalid input
- Lightweight and beginner-friendly project

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- JSON (Exchange Rate Storage)

---

## 📂 Project Structure

Currency_Converter.py
currency.json
README.md


---

## 📄 Required JSON Format (`currency.json`)

Your `currency.json` file should look like this:

```json
{
    "USD": 1,
    "INR": 83,
    "EUR": 0.92,
    "GBP": 0.78
}
💡 Note: USD is used as the base currency (rate = 1).

▶️ How to Run the Project
1️⃣ Make Sure Python is Installed
python --version
2️⃣ Run the Application
python Currency_Converter.py
The Currency Converter window will open.

📝 How It Works
🔹 Enter Amount
Type the amount you want to convert.

🔹 Enter Currency Codes
Enter source currency (e.g., USD)

Enter target currency (e.g., INR)

Currency codes are case-insensitive.

🔹 Click Convert
The application calculates conversion using stored exchange rates.

Result is displayed on the screen.

🔧 Functions Used in Code
Function	Purpose
load_data()	Loads exchange rates from JSON file
convert_currency()	Performs currency conversion
handle_conversion()	Handles user input and displays result
🧮 Conversion Formula Used
Base Amount = amount / rate_of_from_currency
Converted Amount = Base Amount × rate_of_to_currency
