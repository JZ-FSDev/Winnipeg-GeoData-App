document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('execute-btn').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the selected query option
        const selectedQuery = document.getElementById('query-dropdown').value;

        // Check if a query is selected
        if (selectedQuery === "") {
            alert("Please select a query before executing.");
            return; // Stop execution if no query is selected
        }

        // Display "Loading..." message
        const resultsContainer = document.getElementById('results-container');
        resultsContainer.innerHTML = '<p>Loading...</p>';

        // Get form data
        const formData = {
            start_date: document.getElementById('start-date').value,
            start_time: document.getElementById('start-time').value,
            end_date: document.getElementById('end-date').value,
            end_time: document.getElementById('end-time').value,
            street_name: document.getElementById('street-name').value,
            street_type: document.getElementById('street-type').value,
            neighbourhood: document.getElementById('neighbourhood').value,
            num_meters: document.getElementById('num-meters').value,
        };

        // Construct the API endpoint based on the selected query
        const apiEndpoint = '/api/' + selectedQuery;

        // Make a POST request to the server
        fetch(apiEndpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
            .then(response => response.json())
            .then(data => {
                updateMap();

                // Update the results container with the response
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
                    // If no results, display a "Query had no results" message
                    resultsContainer.innerHTML = '<p>Query had no results</p>';
                }
            })
            .catch(error => {
                // Handle errors
                console.error('API Error:', error);

                // Update the results container with the error message
                resultsContainer.innerHTML = '<p>Error: ' + error.message + '</p>';
            })
    });

    // Define a dictionary to map queries to descriptions
    const queryDescriptions = {
        "total_substance_neighbourhood": "List all Neighbourhoods with the total number of Substances used, ordered by the total number of substances in descending order",
        "count_lane_closure_street": "Retrieve the total count of Lane Closures for each Street and Street Type, ordered by Street Name and Street Type",
        "total_wfps_call_neighbourhood": "Retrieve Neighbourhood names along with the total number of houses and the count of WFPS calls for each Neighbourhood, ordered by Neighbourhood name",
        "count_parking_citation_street": "List all Streets along with the count of Parking Citations for each street, ordered by the street name",
        "bus_route_avg_deviation": "Retrieve the Bus Routes along with the average deviation of each stop for each route",
        "street_paystation": "List all Streets and their respective Paystation information, ordered by Street Name",
        "tows_in_neighbourhood": "Find all Tows ids and their status in a given Neighbourhood",
        "bus_route_in_neighbourhood_between_date_time": "List all unique Bus Route numbers, destinations, and names between a given date and time range and neighbourhood",
        "wfps_neighbourhood": "Retrieve the WFPS Call id, date, call time, and reason for a given Neighbourhood",
        "count_bus_stop_street": "List all Streets with the count of Bus Stops on each street, ordered by Street Name",
        "lane_closures_in_neighbourhood": "Find all Lane Closure ids and date ranges in a given Neighbourhood",
        "bus_stops_on_street": "Find all Bus Stop ids, scheduled time, and dates within a given range in meters of all known GPS Points of a given Street Name and Type",
        "parking_citation_and_tow": "Find all Parking Citations ids, fine amounts and types and Tow ids and statuses which occurred on the same location of a given Street name and type",
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


function updateMap() {
    var iframe = document.getElementById("map-iframe");
    iframe.src = iframe.src; // This will trigger a reload of the iframe content.
}