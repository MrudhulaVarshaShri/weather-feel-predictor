# 🌤️ Weather Feel Predictor

An interactive Python application that predicts how the weather feels based on temperature input using a simple distance-based model.

---

## 🚀 Features

- Predicts weather feel (e.g., Cold, Warm, Hot)
- Uses nearest temperature matching logic
- Interactive command-line interface
- Handles invalid inputs gracefully

---

## 🧠 How It Works

The model uses a simple distance-based approach:

1. Predefined dataset with temperature labels
2. Calculates absolute difference between user input and dataset values
3. Selects the closest temperature
4. Returns corresponding weather label

---

## 📊 Sample Data

| Temperature (°C) | Feel        |
|----------------|------------|
| 0              | Freezing ❄️ |
| 10             | Cold 🌬️ |
| 20             | Pleasant 😊 |
| 30             | Warm 🌤️ |
| 40             | Very Hot 🥵 |

---

## ▶️ How to Run

```bash
python main.py

---

## 👤 Author

Mrudhula Varshashri A