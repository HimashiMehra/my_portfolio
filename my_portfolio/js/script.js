document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });
    }

    // 2. Active Link Highlighting
    const links = document.querySelectorAll('.nav-links a');
    links.forEach(link => {
        // Simple active state based on current URL path
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });

    // 3. Contact Form Validation (Client-Side)
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let isValid = true;
            
            // Name validation
            const nameInput = document.getElementById('name');
            if (nameInput && nameInput.value.trim() === '') {
                showError(nameInput, 'Name is required');
                isValid = false;
            } else if (nameInput) {
                removeError(nameInput);
            }
            
            // Email validation
            const emailInput = document.getElementById('email');
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (emailInput && emailInput.value.trim() === '') {
                showError(emailInput, 'Email is required');
                isValid = false;
            } else if (emailInput && !emailPattern.test(emailInput.value.trim())) {
                showError(emailInput, 'Please enter a valid email address');
                isValid = false;
            } else if (emailInput) {
                removeError(emailInput);
            }
            
            // Message validation
            const messageInput = document.getElementById('message');
            if (messageInput && messageInput.value.trim() === '') {
                showError(messageInput, 'Message is required');
                isValid = false;
            } else if (messageInput) {
                removeError(messageInput);
            }
            
            // If not valid, prevent submission
            if (!isValid) {
                e.preventDefault();
            }
        });
    }
    
    function showError(input, message) {
        const formGroup = input.parentElement;
        formGroup.classList.add('error');
        let errorEl = formGroup.querySelector('.error-message');
        if (!errorEl) {
            errorEl = document.createElement('div');
            errorEl.className = 'error-message';
            formGroup.appendChild(errorEl);
        }
        errorEl.textContent = message;
    }
    
    function removeError(input) {
        const formGroup = input.parentElement;
        formGroup.classList.remove('error');
        const errorEl = formGroup.querySelector('.error-message');
        if (errorEl) {
            errorEl.remove();
        }
    }
});
