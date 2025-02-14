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

        // Disable the "Execute" button
        const executeBtn = document.getElementById('execute-btn');
        executeBtn.disabled = true;

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
            .finally(() => {
                // Enable the "Execute" button again after fetch completes (success or error)
                executeBtn.disabled = false;
            });
    });

    // Define a dictionary to map queries to descriptions
    const queryDescriptions = {
        "count_substance_neighbourhood": "Retrieve Neighbourhood names along with the total number of houses and the count of Substance Uses for each Neighbourhood",
        "count_lane_closure_street": "Retrieve the total count of Lane Closures for each Street",
        "count_wfps_call_neighbourhood": "Retrieve Neighbourhood names along with the total number of houses and the count of WFPS calls for each Neighbourhood",
        "count_parking_citation_street": "Retrieve the total count of Parking Citations and the sum of all violation fine amounts for each Street",
        "bus_route_avg_deviation": "Retrieve the Bus Routes along with the average deviation of each stop for each route",
        "street_paystation": "List all Streets and their respective Paystation id, time_limit, and space, ordered by Street name and type. Plots the results in the interactive map",
        "tows_in_neighbourhood": "Find all Tows ids, statuses, dates, and times in a given Neighbourhood. Displays the Tows in the interactive map",
        "bus_route_in_neighbourhood_between_date_time": "List all unique Bus Route numbers, destinations, and names between a given date and time range that run through a given neighbourhood",
        "wfps_in_neighbourhood": "Retrieve all the WFPS Call ids, dates, call times, and reasons for a given Neighbourhood",
        "count_bus_stop_street": "List all Streets with the count of Bus Stops on each street",
        "lane_closures_in_neighbourhood": "Find all Lane Closure ids and date ranges in a given Neighbourhood. Displays the center locations of the Lane Closures on the interactive map",
        "bus_stops_on_street": "Find all Bus Stop ids, scheduled times, dates, and route names within a given range in meters of all known GPS Points of a given Street name and type. Displays the Bus Stops on the interactive map",
        "parking_citation_and_tow_on_street": "Find all Parking Citations ids, fine amounts and types and Tow ids and statuses which occurred on the same location of a given Street name and type. Displays the shared locations of the Tows and Parking Citations on the interative map",
        "transit_delay_due_to_tow": "Transit delays that might have been caused due to Tows happening nearby. Reports nearby Bus Stop id, deviation, route destination, route number, route name, and Tow ids. Displays the locations of the Tows and Bus Stops on the interative map",
        "transit_delay_due_to_citation": "Transit delays that might have been caused due to Parking_Citations nearby. Reports nearby Bus Stop id, deviation, route destination, route number, route name, and Parking Citation ids. Displays the locations of the Parking Citations and Bus Stops on the interative map",
        "substances_in_neighbourhood": "Retrieves all Substance Use ids, dates, times, and substances for a given Neighbourhood",
        "tows_due_to_lane_closures": "Tows that might have happended due to being within a given number of meters to any Lane Closures within a given date-time range. Reports Tow ids and dates and Lane Closure ids, and closure start and end dates"
        // Add more queries and descriptions as needed
    };

    const queryCategories = {
        "count_substance_neighbourhood": ['Substance Abuse', 'Neighbourhood'],
        "count_lane_closure_street": ['Lane Closure', 'Street'],
        "count_wfps_call_neighbourhood": ['WFPS Call', 'Neighbourhood'],
        "count_parking_citation_street": ['Parking Citation', 'Street'],
        "bus_route_avg_deviation": ['Bus Stop', 'Bus Route'],
        "street_paystation": ['Street', 'Paystation', "GPS Point"],
        "tows_in_neighbourhood": ['Tow', 'Neighbourhood', "GPS Point"],
        "bus_route_in_neighbourhood_between_date_time": ['Bus Route', 'Neighbourhood', 'Date-Time'],
        "wfps_in_neighbourhood": ['WFPS Call', 'Neighbourhood'],
        "count_bus_stop_street": ['Bus Stop', 'Street'],
        "lane_closures_in_neighbourhood": ['Lane Closure', 'Neighbourhood', "GPS Point"],
        "bus_stops_on_street": ['Bus Stop', 'Street', "GPS Point"],
        "parking_citation_and_tow_on_street": ['Parking Citation', 'Tow', "GPS Point"],
        "transit_delay_due_to_tow": ['Tow', 'Bus Stop', 'Bus Route', "GPS Point"],
        "transit_delay_due_to_citation": ['Tow', 'Bus Stop', 'Bus Route', "GPS Point"],
        "substances_in_neighbourhood": ['Substance Abuse', 'Neighbourhood'],
        "tows_due_to_lane_closures": ['Tow', 'Lane Closure', 'Date-Time', "GPS Point"]
    }

    const parameterCategories = {
        "count_substance_neighbourhood": [],
        "count_lane_closure_street": [],
        "count_wfps_call_neighbourhood": [],
        "count_parking_citation_street": [],
        "bus_route_avg_deviation": [],
        "street_paystation": [],
        "tows_in_neighbourhood": ['neighbourhood-section'],
        "bus_route_in_neighbourhood_between_date_time": ['neighbourhood-section', 'start-date-time-section', 'end-date-time-section'],
        "wfps_in_neighbourhood": ['neighbourhood-section'],
        "count_bus_stop_street": [],
        "lane_closures_in_neighbourhood": ['neighbourhood-section'],
        "bus_stops_on_street": ['street-section', 'meter-section'],
        "parking_citation_and_tow_on_street": ['street-section'],
        "transit_delay_due_to_tow": [],
        "transit_delay_due_to_citation": [],
        "substances_in_neighbourhood": ['neighbourhood-section'],
        "tows_due_to_lane_closures": ['meter-section', 'start-date-time-section', 'end-date-time-section']

    };

    function updateQueryDescription() {

        const dropdown = document.getElementById("query-dropdown");
        let selectedQuery = dropdown.value; // Store the currently selected option
        const descriptionElement = document.getElementById("query-description");
        const selectedCheckboxes = Array.from(document.querySelectorAll('.checkbox-column input:checked'));
        const selectedCategories = selectedCheckboxes.map(checkbox => checkbox.name);

        const allQueries = Object.keys(queryCategories);

        // Clear existing options
        dropdown.innerHTML = '';

        // Add the static "Select a Query" option
        const defaultOption = document.createElement('option');
        defaultOption.value = "";
        defaultOption.textContent = "Select a Query";
        defaultOption.disabled = true;
        defaultOption.selected = true;
        dropdown.appendChild(defaultOption);

        // If no checkboxes are checked, show all queries
        if (selectedCategories.length === 0) {
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

            // Show the corresponding parameter categories for the selected query
            showParameterCategories(parameterCategories[selectedQuery] || []);

        }

        // Restore the selected option if it still exists
        if (selectedQuery && dropdown.querySelector(`option[value="${selectedQuery}"]`)) {
            dropdown.value = selectedQuery;
        } else {
            // Otherwise, select the default option
            dropdown.value = "";
            selectedQuery = "";
            hideAllParameterCategories();
        }

        // Update the description based on the selected query
        descriptionElement.textContent = queryDescriptions[selectedQuery] || "";
    }

    function hideAllParameterCategories() {
        const allParameterCategories = document.querySelectorAll('.dual-input-container');
        allParameterCategories.forEach(category => {
            category.style.display = 'none';
        });
    }

    function showParameterCategories(categoriesToShow) {
        hideAllParameterCategories();
        categoriesToShow.forEach(category => {
            const div = document.getElementById(category);
            if (div) {
                div.style.display = 'block';
            }
        });
    }

    // Attach the update function to the change event of the dropdown
    document.getElementById("query-dropdown").addEventListener("change", function () {
        // Show the corresponding parameter categories for the selected query
        const selectedQuery = this.value;
        showParameterCategories(parameterCategories[selectedQuery] || []);

        updateQueryDescription();
    });

    // Attach the update function to the change event of checkboxes
    const checkboxes = document.querySelectorAll('.checkbox-column input');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateQueryDescription);
    });

    // Hide all parameter categories
    hideAllParameterCategories();
});

function updateMap() {
    var iframe = document.getElementById("map-iframe");
    iframe.src = iframe.src; // This will trigger a reload of the iframe content.
}