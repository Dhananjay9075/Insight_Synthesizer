from flask import Flask, render_template, request
from utils.gemini import generate_insights

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def input_page():
    if request.method == "POST":
        feedback_raw = request.form.get("feedback")
        feedback_list = [line.strip() for line in feedback_raw.strip().split("\n") if line.strip()]
        insights = generate_insights(feedback_list)
        return render_template("output.html", insights=insights)
    return render_template("input.html")

if __name__ == "__main__":
    app.run(debug=True)
