
import sys
from pathlib import Path

from flask import Flask, render_template, request

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


if __name__ == "__main__":
    app.run(debug=True)
