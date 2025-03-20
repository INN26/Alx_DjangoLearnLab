document.addEventListener("DOMContentLoaded", function () {
    let registerForm = document.querySelector("#registerForm");

    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            let email = document.querySelector("#email").value;
            let password = document.querySelector("#password").value;
            let confirmPassword = document.querySelector("#confirm_password").value;

            if (email === "" || password === "" || confirmPassword === "") {
                event.preventDefault();
                alert("All fields are required!");
            } else if (password !== confirmPassword) {
                event.preventDefault();
                alert("Passwords do not match!");
            }
        });
    }
});