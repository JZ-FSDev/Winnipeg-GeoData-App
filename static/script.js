document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('execute-btn').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get form data
        const formData = new FormData(document.getElementById('query-form'));

        // Make a POST request to the server
        fetch('/submit', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response data
            console.log('API Response:', data);

            // Update the results container with the response
            const resultsContainer = document.getElementById('results-container');
            resultsContainer.innerHTML = '<p>Results:</p>';
            resultsContainer.innerHTML += '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        })
        .catch(error => {
            // Handle errors
            console.error('API Error:', error);

            // Update the results container with the error message
            const resultsContainer = document.getElementById('results-container');
            resultsContainer.innerHTML = '<p>Error: ' + error.message + '</p>';
        });
    });
});
