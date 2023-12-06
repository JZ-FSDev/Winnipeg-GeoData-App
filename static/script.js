document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('execute-btn').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the field data
        const selectedQuery = document.getElementById('query-dropdown').value;
        const start_date = document.getElementById('start-date').value;
        const start_time = document.getElementById('start-time').value;
        const end_date = document.getElementById('end-date').value;
        const end_time = document.getElementById('end-time').value;
        const street_name = document.getElementById('street-name').value;
        const street_type = document.getElementById('street-type').value;
        const neighbourhood = document.getElementById('neighbourhood').value;
        const num_meters = document.getElementById('num-meters').value;

        // Check if a query is selected
        if (selectedQuery === "") {
            alert("Please select a query before executing.");
            return; // Stop execution if no query is selected
        }
        // Check if a neighbourhood is selected
        if (neighbourhood === "") {
            alert("Please select a neighbourhood before executing.");
            return; // Stop execution if no query is selected
        }
        // Check if a date and time range is selected
        if (start_time === "" || start_date === "" || end_time === "" || end_date === "") {
            alert("Please fill in date and time range before executing.");
            return; // Stop execution if no query is selected
        }


        // Display "Loading..." message
        const resultsContainer = document.getElementById('results-container');
        resultsContainer.innerHTML = '<p>Loading...</p>';

        // Get form data
        const formData = {
            start_date: start_date,
            start_time: start_time,
            end_date: end_date,
            end_time: end_time,
            street_name: street_name,
            street_type: street_type,
            neighbourhood: neighbourhood,
            num_meters: num_meters,
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
        "total_wfps_call_neighbourhood": "Retrieve Neighbourhood names along with the total number of houses and the count of WFPS calls for each Neighbourhood, ordered by neighbourhood name",
        "count_parking_citation_street": "List all Streets along with the count of Parking Citations for each street, ordered by street name and type",
        "bus_route_avg_deviation": "Retrieve the Bus Routes along with the average deviation of each stop for each route",
        "street_paystation": "List all Streets and their respective Paystation id, time_limit, and space, ordered by Street name and type. Plots the results in the interactive map",
        "tows_in_neighbourhood": "Find all Tows ids and their status in a given Neighbourhood. Displays the Tows in the interactive map",
        "bus_route_in_neighbourhood_between_date_time": "List all unique Bus Route numbers, destinations, and names between a given date and time range that run through a given neighbourhood",
        "wfps_neighbourhood": "Retrieve the WFPS Call id, date, call time, and reason for a given Neighbourhood",
        "count_bus_stop_street": "List all Streets with the count of Bus Stops on each street, ordered by Street name and type",
        "lane_closures_in_neighbourhood": "Find all Lane Closure ids and date ranges in a given Neighbourhood. Displays the center locations of the Lane Closures on the interactive map",
        "bus_stops_on_street": "Find all Bus Stop ids, scheduled time, and dates and Bus Route name within a given range in meters of all known GPS Points of a given Street name and type. Displays the Bus Stops on the interactive map",
        "parking_citation_and_tow": "Find all Parking Citations ids, fine amounts and types and Tow ids and statuses which occurred on the same location of a given Street name and type. Displays the shared locations of the Tows and Parking Citations",
        // Add more queries and descriptions as needed
    };

    const queryCategories = {
        "total_substance_neighbourhood": ['Substance Abuse', 'Neighbourhood'],
        "count_lane_closure_street": ['Lane Closure', 'Street'],
        "total_wfps_call_neighbourhood": ['WFPS Call', 'Neighbourhood'],
        "count_parking_citation_street": ['Parking Citation', 'Street'],
        "bus_route_avg_deviation": ['Bus Stop', 'Bus Route'],
        "street_paystation": ['Street', 'Paystation'],
        "tows_in_neighbourhood": ['Tow', 'Neighbourhood'],
        "bus_route_in_neighbourhood_between_date_time": ['Bus Route', 'Neighbourhood', 'Date', 'Time'],
        "wfps_neighbourhood": ['WFPS Call', 'Neighbourhood'],
        "count_bus_stop_street": ['Bus Stop', 'Street'],
        "lane_closures_in_neighbourhood": ['Lane Closure', 'Neighbourhood'],
        "bus_stops_on_street": ['Bus Stop', 'Street'],
        "parking_citation_and_tow": ['Parking Citation', 'Tow'],
    }

    function updateQueryDescription() {
        const dropdown = document.getElementById("query-dropdown");
        dropdown.innerHTML = ''; // Clear existing options

        const selectedCheckboxes = Array.from(document.querySelectorAll('.checkbox-column input:checked'));
        const selectedCategories = selectedCheckboxes.map(checkbox => checkbox.name.replace('filter-', ''));

        const allQueries = Object.keys(queryCategories);

        // If no checkboxes are checked, show all queries and add default option
        if (selectedCategories.length === 0) {
            const defaultOption = document.createElement('option');
            defaultOption.value = "";
            defaultOption.textContent = "Select a Query";
            dropdown.appendChild(defaultOption);

            for (const query of allQueries) {
                const option = document.createElement('option');
                option.value = query;
                option.textContent = query;
                dropdown.appendChild(option);
            }
        } else {
            // Filter and add the options to the dropdown based on selected categories
            const queriesToShow = allQueries.filter(query => {
                const categories = queryCategories[query];
                return selectedCategories.every(category => categories.includes(category));
            });

            for (const query of queriesToShow) {
                const option = document.createElement('option');
                option.value = query;
                option.textContent = query;
                dropdown.appendChild(option);
            }
        }

        // Update the description based on the selected query
        const selectedQuery = dropdown.value;
        const descriptionElement = document.getElementById("query-description");
        descriptionElement.textContent = queryDescriptions[selectedQuery] || "";
    }



    // Attach the update function to the change event of the dropdown
    document.getElementById("query-dropdown").addEventListener("change", updateQueryDescription);

    // Attach the update function to the change event of checkboxes
    const checkboxes = document.querySelectorAll('.checkbox-column input');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateQueryDescription);
    });

    // Trigger the update on page load
    // updateQueryDescription();
});

function updateMap() {
    var iframe = document.getElementById("map-iframe");
    iframe.src = iframe.src; // This will trigger a reload of the iframe content.
}