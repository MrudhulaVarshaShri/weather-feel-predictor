from flask import Flask, render_template, request

app = Flask(__name__)

# Store last 5 temperatures
history = []

# Training data
data = {
    0: "Freezing ❄️",
    5: "Very Cold 🧊",
    10: "Cold 🌬️",
    15: "Cool 🌥️",
    20: "Pleasant 😊",
    25: "Comfortable 🙂",
    30: "Warm 🌤️",
    35: "Hot 🔥",
    40: "Very Hot 🥵",
    45: "Extreme Heat 🚨"
}

# Prediction logic (Nearest Neighbor)
def predict_label(user_temp):
    closest_temp = min(data.keys(), key=lambda x: abs(x - user_temp))
    return closest_temp, data[closest_temp]

# Advice logic
def get_advice(label):
    advice_map = {
        "Freezing ❄️": "Wear heavy winter clothes 🧥",
        "Very Cold 🧊": "Layer up and stay warm 🧣",
        "Cold 🌬️": "Keep yourself covered 🧤",
        "Cool 🌥️": "Light jacket recommended 🧥",
        "Pleasant 😊": "Perfect weather, enjoy your day 🌸",
        "Comfortable 🙂": "Great for outdoor activities 🚶",
        "Warm 🌤️": "Stay hydrated 💧",
        "Hot 🔥": "Avoid direct sunlight ☀️",
        "Very Hot 🥵": "Stay indoors and drink water 🥤",
        "Extreme Heat 🚨": "Avoid going outside, stay safe 🚫"
    }
    return advice_map.get(label, "")

# Icon logic
def get_icon(label):
    icon_map = {
        "Freezing ❄️": "❄️",
        "Very Cold 🧊": "🧊",
        "Cold 🌬️": "🌬️",
        "Cool 🌥️": "🌥️",
        "Pleasant 😊": "🌤️",
        "Comfortable 🙂": "🌈",
        "Warm 🌤️": "☀️",
        "Hot 🔥": "🔥",
        "Very Hot 🥵": "🥵",
        "Extreme Heat 🚨": "🚨"
    }
    return icon_map.get(label, "🌡️")


@app.route("/", methods=["GET", "POST"])
def home():
    global history
    result = None

    if request.method == "POST":
        try:
            user_temp = float(request.form["temperature"])

            # Prediction
            closest_temp, label = predict_label(user_temp)

            # Features
            advice = get_advice(label)
            icon = get_icon(label)
            explanation = f"Based on nearest temperature {closest_temp}°C, it feels {label}"

            # Add to history
            history.append(user_temp)

            # Keep only last 5 values
            if len(history) > 5:
                history.pop(0)

            result = {
                "input": user_temp,
                "closest": closest_temp,
                "label": label,
                "advice": advice,
                "explanation": explanation,
                "icon": icon
            }

        except ValueError:
            result = {"error": "Please enter a valid number"}

    return render_template("index.html", result=result, history=history)


if __name__ == "__main__":
    app.run(debug=True)