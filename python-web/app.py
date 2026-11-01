
import sys
from pathlib import Path

from flask import Flask, render_template, request, jsonify

# Add the main project directory to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from calculate import calculate

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    expression = None

    if request.method == "POST":
        try:
            num_1 = float(request.form["num_1"])
            num_2 = float(request.form["num_2"])
            operation = request.form["operation"]

            expression, result = calculate(
                num_1, num_2, operation
            )

        except ValueError as e:
            error = str(e)

        except (KeyError, TypeError):
            error = "Please enter valid inputs."

    return render_template(
        "index.html",
        result=result,
        expression=expression,
        error=error
    )

@app.route("/calculate", methods=["POST"])
def calculate_api():
    try:
        data = request.get_json()

        num_1 = float(data["num_1"])
        num_2 = float(data["num_2"])
        operation = data["operation"]

        expression, result = calculate(
            num_1, num_2, operation
        )

        return jsonify({
            "success": True,
            "expression": expression,
            "result": result
        })

    except (ValueError, KeyError, TypeError) as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400

if __name__ == "__main__":
    app.run(debug=False)
