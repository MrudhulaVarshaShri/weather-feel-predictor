# 🌤️ Weather Feel Predictor

An interactive web application that predicts how the weather feels based on temperature input using a simple distance-based (nearest neighbor) model.

🔗 **Live App:** https://weather-feel-predictor.onrender.com

---

## 🚀 Features

- 🌡️ Predicts weather feel (Cold, Pleasant, Hot, etc.)
- 🧠 Uses nearest temperature matching logic
- 💡 Provides smart advice based on weather conditions
- 📊 Explains how the prediction was made
- 🎨 Clean and responsive UI
- 🌐 Fully deployed web application

---

## 🧠 How It Works

The model uses a simple distance-based approach:

1. Uses a predefined dataset of temperatures and labels  
2. Calculates absolute difference between input and dataset  
3. Finds the closest matching temperature  
4. Returns:
   - Weather label  
   - Explanation  
   - Practical advice  

---

## 📊 Sample Data

| Temperature (°C) | Feel |
|----------------|------|
| 0              | Freezing ❄️ |
| 10             | Cold 🌬️ |
| 20             | Pleasant 😊 |
| 30             | Warm 🌤️ |
| 40             | Very Hot 🥵 |

---

## 🖥️ Tech Stack

- Python (Flask)
- HTML & CSS
- Gunicorn
- Render (Deployment)

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/MrudhulaVarshaShri/weather-feel-predictor.git
cd weather-feel-predictor
pip install -r requirements.txt
python app.py

---

## 👤 Author

**Mrudhula Varshashri A**  
Computer Science Engineer