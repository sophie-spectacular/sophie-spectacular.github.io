// include.js

// Function to fetch and insert header content
function includeHeader() {
    fetch('includes/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-placeholder').innerHTML = data;
        })
        .catch(error => console.error('Error fetching header:', error));
}

// Function to fetch and insert footer content
function includeFooter() {
    fetch('includes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-placeholder').innerHTML = data;
        })
        .catch(error => console.error('Error fetching footer:', error));
}

// Call the functions to include header and footer
includeHeader();
includeFooter();
