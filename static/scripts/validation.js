const password1Input = document.getElementById("pass1");
const password2Input = document.getElementById("pass2");
const passwordMatchMessage = document.getElementById("passwordMatchMessage");
const button = document.getElementById("submitBtn");
const phone = document.getElementById("phone");

password2Input.addEventListener("input", () => {
    const password1Value = password1Input.value;
    const password2Value = password2Input.value;

    if (password1Value === password2Value) {
    passwordMatchMessage.textContent = "Passwords match";
    passwordMatchMessage.classList.remove("incorrect-password");
    passwordMatchMessage.classList.add("correct-password");
    button.disabled = false;
    } else {
    passwordMatchMessage.textContent = "Passwords do not match";
    passwordMatchMessage.classList.remove("correct-password");
    passwordMatchMessage.classList.add("incorrect-password");
    button.disabled = true;
    }
});

input.addEventListener("input", function() {
    const value = this.value;

    if (value.length > 10) {
      button.disabled = false;
    } else {
        button.disabled = true;
    }
  });