# Basic Calculator

A multi-platform calculator project built using Python, Flask, HTML, CSS, and JavaScript. It includes a command-line calculator, an interactive web calculator, and a REST API.

## 🚀 Live Demos

| Application | Live Link |
|---|---|
| JavaScript Calculator | [Open My Calculator](https://vkaashkrsah.github.io/calculator/) |
| Python Flask Calculator | [Open Flask Calculator](https://calculator-flask-app-68gz.onrender.com) |

## Features

### Python CLI Calculator
- Addition, subtraction, multiplication, and division
- Modulus and percentage calculations
- Decimal number support
- Input validation and exception handling
- Division-by-zero and modulus-by-zero handling

### Flask Web Calculator
- Interactive calculator interface
- Flask-powered backend
- REST API for mathematical operations
- JSON request and response handling
- Shared calculation logic with the Python CLI

### JavaScript Calculator
- Browser-based calculator
- Interactive user interface
- Decimal number support
- Keyboard support
- Calculation history
- Clear and delete functionality

### Automated Testing
- Unit tests using Pytest
- Automated linting using Flake8
- GitHub Actions continuous integration

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Languages | Python, JavaScript |
| Frontend | HTML5, CSS3 |
| Backend | Flask |
| Production Server | Gunicorn |
| Testing | Pytest |
| Code Quality | Flake8 |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Hosting | GitHub Pages, Render |
| API Testing | Postman |

## Project Structure

```text
calculator/
│
├── calculate.py
│
├── python-web/
│   ├── app.py
│   ├── requirements.txt
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       └── index.html
│
├── docs/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   └── test_calculate.py
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vkaashkrsah/calculator.git
```

### 2. Navigate to the Project

```bash
cd calculator
```

### 3. Run the Python CLI Calculator

Make sure Python 3 is installed.

```bash
python3 calculate.py
```

### 4. Run the Flask Web Application

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r python-web/requirements.txt
```

Start the Flask application:

```bash
python -m flask --app python-web.app run
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

### 5. Run Automated Tests

```bash
python -m pytest -v
```

## REST API

The Flask application provides a REST API for calculator operations.

**Endpoint**

```text
POST /calculate
```

**Request Body**

```json
{
    "num_1": 20,
    "num_2": 10,
    "operation": "addition"
}
```

**Successful Response**

```json
{
    "success": true,
    "expression": "20 + 10",
    "result": 30.0
}
```

**Error Handling**

The API returns HTTP 400 for invalid operations, invalid input, and division or modulus by zero.

## Deployment

- **GitHub Pages:** Hosts the standalone JavaScript calculator.
- **Render:** Hosts the Python Flask application.

## Future Improvements

- [ ] Add scientific calculator operations.
- [ ] Add automated API tests.
- [ ] Improve mobile responsiveness.
- [ ] Add more calculation history features.
- [ ] Expand test coverage.

## Author

**Vikash Kumar Sah**

- GitHub: [@vkaashkrsah](https://github.com/vkaashkrsah)
- LinkedIn: [Vikash Kumar Sah](https://www.linkedin.com/in/vkaashkrsah/)

## License

This project is open-source and intended for learning and educational purposes.