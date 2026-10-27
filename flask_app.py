from flask import Flask, render_template, jsonify
from tester.runner import execute_test_suite
from storage import list_runs

app = Flask(__name__)

@app.route("/")
def home():
    return "Atelier Automatisation des tests - API Flask active !"

@app.route("/run")
def run_tests():
    result = execute_test_suite()
    return jsonify({"message": "Tests exécutés avec succès", "result": result})

@app.route("/dashboard")
def dashboard():
    runs = list_runs(limit=20)
    return render_template("dashboard.html", runs=runs)

if __name__ == "__main__":
    app.run(debug=True)
