// Main JavaScript for Loon Tracks website

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNav = document.querySelector('.mobile-navigation');

    if (mobileToggle && mobileNav) {
        mobileToggle.addEventListener('click', function() {
            mobileNav.style.display = mobileNav.style.display === 'block' ? 'none' : 'block';
            mobileToggle.classList.toggle('active');
        });
    }

    // Search functionality
    const searchInput = document.getElementById('search-input');
    const contentGrid = document.getElementById('content-grid');

    if (searchInput && contentGrid) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const articles = contentGrid.querySelectorAll('.content-card');

            articles.forEach(article => {
                const title = article.querySelector('h2').textContent.toLowerCase();
                const summary = article.querySelector('.card-summary').textContent.toLowerCase();

                if (title.includes(searchTerm) || summary.includes(searchTerm)) {
                    article.style.display = 'block';
                } else {
                    article.style.display = 'none';
                }
            });
        });
    }

    // Category filter
    const categoryFilter = document.getElementById('category-filter');

    if (categoryFilter && contentGrid) {
        categoryFilter.addEventListener('change', function() {
            const selectedCategory = this.value.toLowerCase();
            const articles = contentGrid.querySelectorAll('.content-card');

            articles.forEach(article => {
                const categories = article.dataset.categories.toLowerCase();

                if (!selectedCategory || categories.includes(selectedCategory)) {
                    article.style.display = 'block';
                } else {
                    article.style.display = 'none';
                }
            });
        });
    }

    // Newsletter form handling
    const newsletterForm = document.querySelector('.newsletter-form');

    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            // Form will be handled by Netlify, but we can add feedback
            const button = this.querySelector('button');
            const originalText = button.textContent;

            button.textContent = 'Subscribing...';
            button.disabled = true;

            // Re-enable after 3 seconds (Netlify will handle the actual submission)
            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
            }, 3000);
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));

            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Dashboard integration placeholder
    function loadDashboard() {
        // This will be integrated with your forecast system
        const dashboardContainer = document.querySelector('.dashboard-container');

        if (dashboardContainer) {
            // Placeholder for dashboard loading logic
            console.log('Dashboard container found, ready for forecast integration');
        }
    }

    loadDashboard();
});