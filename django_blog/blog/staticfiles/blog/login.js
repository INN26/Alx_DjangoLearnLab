document.addEventListener("DOMContentLoaded", function () {
    let loginForm = document.querySelector("#loginForm");

    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            let email = document.querySelector("#email").value;
            let password = document.querySelector("#password").value;

            if (email === "" || password === "") {
                event.preventDefault();
                alert("All fields are required!");
            }
        });
    }
});