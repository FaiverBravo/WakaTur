

var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

var grayscale   = L.tileLayer(mbUrl, {id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr}),
    streets  = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr}),
    dark  = L.tileLayer(mbUrl, {id: 'mapbox/dark-v10', tileSize: 512, zoomOffset: -1, attribution: mbAttr}),
    outdoors  = L.tileLayer(mbUrl, {id: 'mapbox/outdoors-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});


// Marker Turismo
var turismoIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-green.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var turismo = L.layerGroup();

L.marker([1.887648, -76.2949629],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Parque arquelógico San Agustín</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88724803,-76.29549695],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Museo Arqueológico</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88663907,-76.29590293],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Bosque de las Estatuas</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88303662, -76.2943809],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Mesita A</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88419942, -76.29612945],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Mesita B</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88068292,-76.29795741],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Mesita C</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88077357,-76.29916174],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Fuente Ceremonial de Lavapatas</h2><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo),
L.marker([1.88043362, -76.30314752],{icon: turismoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Alto de Lavapatas</h3><img width="70%" height="70%"src="images/lavapatas.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(turismo);

// Marker Alojamientos
var alojIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-violet.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var alojamientos = L.layerGroup();

L.marker([1.884916, -76.281095],{icon: alojIcon}).bindPopup('<b>Hotel Arqueologico San Agustin</b>').addTo(alojamientos),
L.marker([1.890318, -76.283683],{icon: alojIcon}).bindPopup('<b>Hotel Alto de los Andaquies</b>').addTo(alojamientos),
L.marker([1.892315, -76.281074],{icon: alojIcon}).bindPopup('<b>Akawanka Lodge</b>').addTo(alojamientos);

// Marker Gastroomía
var gastrIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-gold.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var gastronomia = L.layerGroup();

L.marker([1.886524, -76.27747],{icon: gastrIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Restaurante Pepe Nero</h2><img width="70%" height="70%"src="images/r1.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(gastronomia),
L.marker([1.885837,-76.275916],{icon: gastrIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Andrés A La Parrilla</h2><img width="70%" height="70%"src="images/r1.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(gastronomia),
L.marker([1.88701,-76.279091],{icon: gastrIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Donde Richard</h2><img width="70%" height="70%"src="images/r1.jpg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(gastronomia);

// Marker Aventura
var aventuraIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-blue.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var aventura = L.layerGroup();

L.marker([1.885647, -76.275032],{icon: aventuraIcon}).bindPopup('<b>Alquiler de Caballos</b>').addTo(aventura),
L.marker([1.882203, -76.277286],{icon: aventuraIcon}).bindPopup('<b>Magdalena Rafting</b>').addTo(aventura),
L.marker([1.882963, -76.252714],{icon: aventuraIcon}).bindPopup('<b>Adrenalina Extrema Cañon del Magdalena</b>').addTo(aventura);

// Marker Servicios
var serviIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-grey.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var servicios = L.layerGroup();

L.marker([1.881476, -76.270762],{icon: serviIcon}).bindPopup('<b>Cajero ATH Utrahuilca San Agustin I - Banco de Bogotá</b>').addTo(servicios),
L.marker([1.879131, -76.270065],{icon: serviIcon}).bindPopup('<b>Estacion de gasolina, Sur Andina TERPEL</b>').addTo(servicios),
L.marker([1.881455, -76.271182],{icon: serviIcon}).bindPopup('<b>Taxis Verdes</b>').addTo(servicios);

// Marker Tiendas
var tiendaIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-orange.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var tiendas = L.layerGroup();

L.marker([1.884632, -76.273579],{icon: tiendaIcon}).bindPopup('<b>Artesanías</b>').addTo(tiendas),
L.marker([1.880257, -76.271148],{icon: tiendaIcon}).bindPopup('<b>Plaza de Mercado Campesino</b>').addTo(tiendas),
L.marker([1.881822, -76.273193],{icon: tiendaIcon}).bindPopup('<b>Supermercado Olimpica</b>').addTo(tiendas);

// Marker Contacto
var contactoIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-icon-2x-green.png',
    shadowUrl: 'images/mapa/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var contacto = L.layerGroup();

L.marker([1.8862233, -76.277418],{icon: contactoIcon}).bindPopup('<div align="center"style= "heigth: 150px; width:200px"><h2>Locate</h2> <p>Publica con nosotros</p><img width="70%" height="70%"src="images/logof.svg"><p>informate <a href="https://faiverbravo.github.io/locate/">aca</a></p></div>').addTo(contacto);
  
//--Geolocalización marker"
var geoIcon = new L.Icon({
    iconUrl: 'images/mapa/marker-yo.png',
    iconSize: [45, 65],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    });

//--Mostrar Mapa
    var map = L.map('map', {
        layers: [grayscale, turismo, alojamientos, gastronomia],
        scrollWheelZoom:false,
        });

    //--Geolocalización "Estas Aquí!"
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);
	
	function buscarLocalizacion(e) {
		L.marker(e.latlng,{icon: geoIcon}).bindPopup('<b>Estoy Aquí !</b>').addTo(map);
		}
	
	function errorLocalizacion(e) {
		alert("No es posible encontrar su ubicación. Es posible que tenga que activar la geolocalización. Prueba con Firefox ;-)");
}
	map.on('locationerror', errorLocalizacion);
	map.on('locationfound', buscarLocalizacion);
	map.locate({setView: true, maxZoom:15});
	    
//--Establecemos var capas base
var baseLayers = {
    "Grayscale": grayscale,
    "Streets": streets,
    "Dark": dark,
    "Outdoors": outdoors,
    
};

//--capas para mostrar por separado Markers
var overlays = {
    "Turismo": turismo,
    "Alojamientos": alojamientos,
    "Gastronomía": gastronomia,
    "Aventura": aventura,
    "Servicios": servicios,
    "Tiendas": tiendas
};

L.control.layers(baseLayers, overlays).addTo(map);

//--mostrar escala y logo
L.control.scale({
    metric:true,
    imperial:false,
    position:'topright',
}).addTo(map);

L.Control.Watermark=L.Control.extend({
    onAdd:function(map){
        var img=L.DomUtil.create('img');
        img.src='images/milestone_1.png';
        img.style.width='40px';
        return img;
    },
    onRemove:function(map){},
})
    L.control.watermark=function(opts){
        return new L.Control.Watermark({opts});
    }
    L.control.watermark().addTo(map);

	

	
    