// Function to load locations from the server and populate the dropdown
function onPageLoad() {
    console.log("Document loaded");

    // URL to get the location names
    var url = "https://bangalore-house-price-prediction-iq48.onrender.com/get_location_names"; // Updated URL for getting location names

    // Fetch the location names
    $.get(url, function(data, status) {
        console.log("Got response for get_location_names request");

        if (data && data.locations) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");

            // Clear existing options in the dropdown
            $('#uiLocations').empty();

            // Add a default option
            var defaultOption = new Option("Choose a Location", "");
            $('#uiLocations').append(defaultOption);

            // Add options to the dropdown
            for (var i in locations) {
                var opt = new Option(locations[i], locations[i]);
                $('#uiLocations').append(opt);
            }
        } else {
            console.error("No location data found");
        }
    }).fail(function() {
        console.error("Failed to fetch location names");
    });
}

// Call the function when the window loads
window.onload = onPageLoad;

// Function to get the selected BHK value from radio buttons
function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; // Invalid Value
}

// Function to get the selected Bath value from radio buttons
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; // Invalid Value
}

// Function to get the selected location value from the dropdown
function getSelectedLocation() {
    var locationDropdown = document.getElementById("uiLocations");
    return locationDropdown.value;
}

// Function to handle the button click event to estimate price
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    
    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue(); 
    var bathrooms = getBathValue(); 
    var location = getSelectedLocation();
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "https://bangalore-house-price-prediction-iq48.onrender.com/predict_home_price"; // Updated URL for predicting price

    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            total_sqft: parseFloat(sqft),
            bhk: bhk,
            bath: bathrooms,
            location: location
        }),
        success: function(data, status) {
            if (data.error) {
                estPrice.innerHTML = "<h2>Error: " + data.error + "</h2>";
            } else {
                estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
            }
            console.log(status);
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
            estPrice.innerHTML = "<h2>Error: " + error + "</h2>";
        }
    });
}
