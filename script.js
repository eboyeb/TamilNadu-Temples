// Initialize the map
var map = L.map('map').setView([11.1271, 78.6569], 7);

// Add the OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Load the temple data
fetch('temples_geocoded.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(temples => {
        // Create a feature group to hold all markers
        const markerGroup = L.featureGroup().addTo(map);

        temples.forEach(temple => {
            if (temple.coordinates && Array.isArray(temple.coordinates) && temple.coordinates.length === 2) {
                L.marker(temple.coordinates)
                    .bindPopup(`<b>${temple.name}</b><br>${temple.location}`)
                    .addTo(markerGroup);
            }
        });

        // Fit the map to show all markers
        map.fitBounds(markerGroup.getBounds());
    })
    .catch(error => {
        console.error('Error loading temple data:', error);
        // Optionally, display an error message to the user
    });