    // Get the form element
    const form = document.getElementById('signupForm');

    // Function to handle form submission
    const handleSubmit = (event) => {
        // Prevent form submission
        event.preventDefault();

        // Validate the form
        if (form.checkValidity()) {
            // If the form is valid, submit it
            form.submit();
        } else {
            // If the form is invalid, display error messages
            form.reportValidity();
        }
    };

    // Attach form submission handler to the submit event
    form.addEventListener('submit', handleSubmit);
const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');
    
    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });
    
    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
    });
    const passwordPattern = /^(?=.*\d)(?=.*[!@#$%^&*()])[a-zA-Z0-9!@#$%^&*()]{8,}$/;

const isPasswordValid = () => {
  const passwordInput = document.getElementById('mdp');
  const password = passwordInput.value;

  if (passwordPattern.test(password)) {
    passwordInput.classList.remove('error');
    passwordInput.setCustomValidity('');
    return true;
  } else {
    passwordInput.classList.add('error');
    passwordInput.setCustomValidity('Password must contain at least one digit and one special character');
    return false;
  }
};

const isPhoneNumberValid = () => {
  const phoneNumberInput = document.getElementById('PhoneNumber');
  const phoneNumber = phoneNumberInput.value;

  if (/^\d{8}$/.test(phoneNumber)) {
    phoneNumberInput.classList.remove('error');
    phoneNumberInput.setCustomValidity('');
    return true;
  } else {
    phoneNumberInput.classList.add('error');
    phoneNumberInput.setCustomValidity('Phone number must contain 8 digits');
    return false;
  }
};

const isDateValid = () => {
  const dateInput = document.getElementById('date');
  const dateValue = dateInput.value;

  const selectedDate = new Date(dateValue);
  const currentDate = new Date();

  if (selectedDate < currentDate) {
    dateInput.classList.remove('error');
    dateInput.setCustomValidity('');
    return true;
  } else {
    dateInput.classList.add('error');
    dateInput.setCustomValidity('Date must be earlier than today');
    return false;
  }
};

const signupForm = document.getElementById('signupForm');
signupForm.addEventListener('submit', (e) => {
  if (!isPasswordValid() || !isPhoneNumberValid() || !isDateValid()) {
    e.preventDefault();
  }
});

const passwordInput = document.getElementById('mdp');
passwordInput.addEventListener('input', () => {
  isPasswordValid();
});

const phoneNumberInput = document.getElementById('PhoneNumber');
phoneNumberInput.addEventListener('input', isPhoneNumberValid);

const dateInput = document.getElementById('date');
dateInput.addEventListener('input', isDateValid);