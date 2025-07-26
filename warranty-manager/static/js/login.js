document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    const errorDiv = document.getElementById('error-message');

    form.addEventListener('submit', function(e) {
        errorDiv.style.display = 'none';
        errorDiv.textContent = '';

        const username = form.querySelector('input[name="username"]');
        const password = form.querySelector('input[name="password"]');

        if (!username.value.trim() || !password.value.trim()) {
            errorDiv.textContent = "Please fill in both fields.";
            errorDiv.style.display = 'block';
            e.preventDefault();
        }
    });
});
