// script.js
document.addEventListener('DOMContentLoaded', function () {
    // Add click event listeners to handle answer selection on div click
    const options = document.querySelectorAll('.option');
    const radioInputs = document.querySelectorAll('input[type="radio"]');

    options.forEach((option, index) => {
        option.addEventListener('click', () => {
            // Toggle the 'selected' class on the clicked option
            options.forEach((opt) => {
                opt.classList.remove('selected');
            });
            option.classList.add('selected');

            // Programmatically select the associated radio button
            radioInputs[index].checked = true;
        });
    });

    // Add event listener to handle form submission
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', function () {
        // Capture the selected answer and set it as the value of the hidden input
        const selectedOption = document.querySelector('.selected');
        if (selectedOption) {
            const selectedAnswer = selectedOption.textContent;
            document.getElementById('selected-choice').value = selectedAnswer;
        } else {
            alert('Please select an answer before submitting.');
            event.preventDefault(); // Prevent form submission if no option is selected
        }
    });
});
const form = document.getElementById("my-form");
const loadingIndicator = document.getElementById("loading-indicator");
form.addEventListener("submit", function (e) {
e.preventDefault();
loadingIndicator.style.display = "block";
form.submit();
});

const form2 = document.getElementById("my-form-2");
const loadingIndicator2 = document.getElementById("loading-indicator");
form2.addEventListener("submit", function (e) {
e.preventDefault();
loadingIndicator2.style.display = "block";
form.submit();
});
                                                