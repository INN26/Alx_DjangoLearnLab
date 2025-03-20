document.addEventListener("DOMContentLoaded", function() {
    const formInputs = document.querySelectorAll("input");

    formInputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.borderColor = "#007bff";
        });

        input.addEventListener("blur", () => {
            input.style.borderColor = "#ccc";
        });
    });
});