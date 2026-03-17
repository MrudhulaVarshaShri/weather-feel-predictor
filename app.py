from flask import Flask, render_template, request

app = Flask(__name__)

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

def predict_label(user_temp):
    closest_temp = min(data.keys(), key=lambda x: abs(x - user_temp))
    return closest_temp, data[closest_temp]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            user_temp = float(request.form["temperature"])
            closest_temp, label = predict_label(user_temp)

            result = {
                "input": user_temp,
                "closest": closest_temp,
                "label": label
            }

        except:
            result = {"error": "Invalid input"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)