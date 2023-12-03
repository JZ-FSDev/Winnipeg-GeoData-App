document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('execute-btn').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get form data
        const formData = new FormData(document.getElementById('query-form'));

        // Get the selected query option
        const selectedQuery = document.getElementById('query-dropdown').value;

        // Construct the API endpoint based on the selected query
        const apiEndpoint = '/api/' + selectedQuery;

        // Make a POST request to the server
        fetch(apiEndpoint, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response data
            console.log('API Response:', data);

            // Update the results container with the response
            const resultsContainer = document.getElementById('results-container');
            
            // Check if there are results
            if (data.result && data.result.length > 0) {
                // Build the table dynamically
                const table = document.createElement('table');
                const thead = document.createElement('thead');
                const tbody = document.createElement('tbody');

                // Create header row
                const headerRow = document.createElement('tr');
                for (const key in data.result[0]) {
                    const th = document.createElement('th');
                    th.textContent = key;
                    headerRow.appendChild(th);
                }
                thead.appendChild(headerRow);
                table.appendChild(thead);

                // Create body rows
                data.result.forEach(item => {
                    const tr = document.createElement('tr');
                    for (const key in item) {
                        const td = document.createElement('td');
                        td.textContent = item[key];
                        tr.appendChild(td);
                    }
                    tbody.appendChild(tr);
                });

                table.appendChild(tbody);

                // Clear previous results and append the new table
                resultsContainer.innerHTML = '';
                resultsContainer.appendChild(table);
            } else {
                // If no results, display a "No Results" message
                resultsContainer.innerHTML = '<p>No Results</p>';
            }
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



document.addEventListener("DOMContentLoaded", function () {
    // Define a dictionary to map queries to descriptions
    const queryDescriptions = {
        "total_substance_neighbourhood": "List all Neighbourhoods with the total number of Substances used, ordered by the total number of substances in descending order",
        "count_lane_closure_street": "Retrieve the total count of Lane Closures for each Street and Street Type, ordered by Street Name and Street Type",
        "Query3": "Description for Query3",
        // Add more queries and descriptions as needed
    };

    // Function to update the query description
    function updateQueryDescription() {
        const dropdown = document.getElementById("query-dropdown");
        const selectedQuery = dropdown.value;
        const descriptionElement = document.getElementById("query-description");

        // Update the description based on the selected query
        descriptionElement.textContent = queryDescriptions[selectedQuery] || "";
    }

    // Attach the update function to the change event of the dropdown
    document.getElementById("query-dropdown").addEventListener("change", updateQueryDescription);
    
    // Trigger the update on page load
    updateQueryDescription();
});

