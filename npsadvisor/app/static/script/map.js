var map = L.map('map').setView([39.0997, -97.9903], 4.5);
L.tileLayer('http://{s}.google.com/vt?lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3'],
    attribution: '&copy; <a href="https://www.google.com/intl/en_us/help/terms_maps/">Google Maps</a>'
}).addTo(map);``