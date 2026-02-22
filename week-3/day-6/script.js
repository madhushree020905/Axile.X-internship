// 1️⃣ Alert on Button Click
function showAlert() {
    alert("Button Clicked Successfully!");
}



// 2️⃣ Form Validation
function validateForm() {

    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;

    if (name === "" || email === "") {
        alert("All fields are required!");
        return false;
    }

    alert("Form Submitted Successfully!");
    return true;
}



// 3️⃣ Simple Calculator
function calculate() {

    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    var operator = document.getElementById("operator").value;

    var result;

    if (operator === "+") {
        result = num1 + num2;
    }
    else if (operator === "-") {
        result = num1 - num2;
    }
    else if (operator === "*") {
        result = num1 * num2;
    }
    else if (operator === "/") {
        if (num2 === 0) {
            alert("Cannot divide by zero!");
            return;
        }
        result = num1 / num2;
    }

    document.getElementById("result").innerText = "Result: " + result;
}



// 4️⃣ Change Text on Click
function changeText() {
    document.getElementById("text").innerText = "Text Changed Successfully!";
}