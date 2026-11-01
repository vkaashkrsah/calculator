
const display = document.getElementById("display");
const expressionDisplay = document.getElementById("expression");
const historyList = document.getElementById("history-list");

let currentInput = "0";
let firstNumber = null;
let selectedOperation = null;
let waitingForSecondNumber = false;
let calculationHistory = [];

function updateDisplay() {
    display.textContent = currentInput;
}

function enterNumber(number) {
    if (waitingForSecondNumber) {
        currentInput = number;
        waitingForSecondNumber = false;
    } else {
        currentInput = currentInput === "0"
            ? number
            : currentInput + number;
    }

    updateDisplay();
}

function enterDecimal() {
    if (waitingForSecondNumber) {
        currentInput = "0.";
        waitingForSecondNumber = false;
    } else if (!currentInput.includes(".")) {
        currentInput += ".";
    }

    updateDisplay();
}

function chooseOperation(operation) {
    firstNumber = Number(currentInput);
    selectedOperation = operation;
    waitingForSecondNumber = true;

    const symbols = {
        "+": "+",
        "-": "−",
        "*": "×",
        "/": "÷",
        "%": "%"
    };

    expressionDisplay.textContent =
        `${currentInput} ${symbols[operation]}`;

    if (operation === "percentage") {
        expressionDisplay.textContent =
            `${currentInput}% of`;
    }
}

function calculateResult() {
    if (selectedOperation === null || waitingForSecondNumber) {
        return;
    }

    const secondNumber = Number(currentInput);
    let result;

    try {
        switch (selectedOperation) {
            case "+":
                result = firstNumber + secondNumber;
                break;

            case "-":
                result = firstNumber - secondNumber;
                break;

            case "*":
                result = firstNumber * secondNumber;
                break;

            case "/":
                if (secondNumber === 0) {
                    throw new Error("Cannot divide by zero");
                }
                result = firstNumber / secondNumber;
                break;

            case "%":
                if (secondNumber === 0) {
                    throw new Error("Cannot use modulus by zero");
                }
                result = firstNumber % secondNumber;
                break;

            case "percentage":
                result = (firstNumber / 100) * secondNumber;
                break;

            default:
                return;
        }

        if (!Number.isFinite(result)) {
            throw new Error("Invalid calculation");
        }

        const symbols = {
            "+": "+",
            "-": "−",
            "*": "×",
            "/": "÷",
            "%": "%",
            "percentage": "% of"
        };

        const operator = symbols[selectedOperation];
        const expression = selectedOperation === "percentage"
            ? `${firstNumber}% of ${secondNumber}`
            : `${firstNumber} ${operator} ${secondNumber}`;

        const formattedResult = Number(result.toPrecision(12));

        expressionDisplay.textContent = expression;
        currentInput = String(formattedResult);
        updateDisplay();

        addToHistory(`${expression} = ${formattedResult}`);

        firstNumber = null;
        selectedOperation = null;
        waitingForSecondNumber = true;

    } catch (error) {
        expressionDisplay.textContent = error.message;
        currentInput = "0";
        updateDisplay();

        firstNumber = null;
        selectedOperation = null;
        waitingForSecondNumber = false;
    }
}

function clearCalculator() {
    currentInput = "0";
    firstNumber = null;
    selectedOperation = null;
    waitingForSecondNumber = false;

    expressionDisplay.textContent = "";
    updateDisplay();
}

function deleteLastDigit() {
    if (waitingForSecondNumber) {
        return;
    }

    currentInput = currentInput.length > 1
        ? currentInput.slice(0, -1)
        : "0";

    if (currentInput === "-") {
        currentInput = "0";
    }

    updateDisplay();
}

function addToHistory(entry) {
    calculationHistory.unshift(entry);

    const item = document.createElement("li");
    item.textContent = entry;

    historyList.prepend(item);
}

function clearHistory() {
    calculationHistory = [];
    historyList.innerHTML = "";
}

// Handle calculator button clicks
document.querySelector(".calculator-buttons").addEventListener("click", (event) => {
    const button = event.target.closest("button");

    if (!button) return;

    if (button.dataset.number !== undefined) {
        enterNumber(button.dataset.number);
        return;
    }

    const action = button.dataset.action;

    switch (action) {
        case "decimal":
            enterDecimal();
            break;

        case "operator":
            chooseOperation(button.dataset.value);
            break;

        case "modulus":
            chooseOperation("%");
            break;

        case "percentage":
            chooseOperation("percentage");
            break;

        case "equals":
            calculateResult();
            break;

        case "clear":
            clearCalculator();
            break;

        case "delete":
            deleteLastDigit();
            break;
    }
});

document.getElementById("clear-history")
    .addEventListener("click", clearHistory);

// Keyboard support
document.addEventListener("keydown", (event) => {
    if (/^[0-9]$/.test(event.key)) {
        enterNumber(event.key);
    } else if (event.key === ".") {
        enterDecimal();
    } else if (["+", "-", "*", "/"].includes(event.key)) {
        chooseOperation(event.key);
    } else if (event.key === "%") {
        chooseOperation("%");
    } else if (event.key === "Enter" || event.key === "=") {
        calculateResult();
    } else if (event.key === "Backspace") {
        deleteLastDigit();
    } else if (event.key === "Escape") {
        clearCalculator();
    }
});
