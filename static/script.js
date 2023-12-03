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
        
            if (data.result.length > 0) {
                // Create a table element
                const table = document.createElement('table');
        
                // Create table header
                const headerRow = table.insertRow();
                const headerNeighbourhood = headerRow.insertCell(0);
                headerNeighbourhood.textContent = 'Neighbourhood';
                const headerCount = headerRow.insertCell(1);
                headerCount.textContent = 'Count';
        
                // Populate table with data
                data.result.forEach(item => {
                    const row = table.insertRow();
                    const cellNeighbourhood = row.insertCell(0);
                    cellNeighbourhood.textContent = item.neighbourhood;
                    const cellCount = row.insertCell(1);
                    cellCount.textContent = item.count;
                });
        
                // Append the table to the results container
                resultsContainer.appendChild(table);
            } else {
                // Display a message if there are no results
                resultsContainer.innerHTML += '<p>No Results</p>';
            }
        })
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

