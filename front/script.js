
const displayResult = document.getElementById("display-result");
const displayExpression = document.getElementById("display-expression");

let currentInput = "0";      // número que o usuário está digitando
let previousValue = null;    // primeiro operando
let currentOp = null;        // operação (+, -, *, /, ^)
let waitingForSecond = false;

function formatDisplay(value) {
  // interno usamos ponto, no visor mostramos vírgula
  return String(value).replace(".", ",");
}

function updateDisplay() {
  displayResult.textContent = formatDisplay(currentInput);
}

const API_URL = "http://localhost:5000/calc";

async function sendToBackend(a, op, b = null) {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ a, op, b })
  });
  const data = await res.json();
  if (data.error) throw new Error(data.error);
  return data.result;
}

// ----- handlers -----

function handleNumber(num) {
  if (waitingForSecond) {
    currentInput = num === "." ? "0." : num;
    waitingForSecond = false;
  } else {
    if (num === ".") {
      if (currentInput.includes(".")) return;
      currentInput += ".";
    } else {
      currentInput = currentInput === "0" ? num : currentInput + num;
    }
  }
  updateDisplay();
}

function handleClear() {
  currentInput = "0";
  previousValue = null;
  currentOp = null;
  waitingForSecond = false;
  displayExpression.textContent = "";
  updateDisplay();
}

function handleOp(op) {
  if (op === "sqrt") {
    // raiz é unária: manda direto pro backend
    displayExpression.textContent = `√(${formatDisplay(currentInput)})`;
    sendToBackend(currentInput, "sqrt")
      .then(result => {
        currentInput = String(result);
        updateDisplay();
      })
      .catch(() => (displayResult.textContent = "ERR"));
    return;
  }

  // operação binária
  previousValue = currentInput;
  currentOp = op;
  waitingForSecond = true;
  displayExpression.textContent = `${formatDisplay(previousValue)} ${op}`;
}

function handleEqual() {
  if (!currentOp || previousValue === null) return;

  const a = previousValue;
  const b = currentInput;

  displayExpression.textContent = `${formatDisplay(a)} ${currentOp} ${formatDisplay(b)} =`;

  sendToBackend(a, currentOp, b)
    .then(result => {
      currentInput = String(result);
      previousValue = null;
      currentOp = null;
      waitingForSecond = false;
      updateDisplay();
    })
    .catch(() => (displayResult.textContent = "ERR"));
}

// ----- binding dos botões -----

document.querySelectorAll("[data-num]").forEach(btn => {
  btn.addEventListener("click", () => {
    const raw = btn.getAttribute("data-num");
    const num = raw === "," ? "." : raw;
    handleNumber(num);
  });
});

document.querySelectorAll("[data-op]").forEach(btn => {
  btn.addEventListener("click", () => {
    const op = btn.getAttribute("data-op");
    handleOp(op);
  });
});

document.querySelectorAll("[data-action]").forEach(btn => {
  btn.addEventListener("click", () => {
    const action = btn.getAttribute("data-action");
    if (action === "clear") handleClear();
    if (action === "equal") handleEqual();
  });
});

// inicia visor
updateDisplay();
