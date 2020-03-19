$.getJSON("https://openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22", function(data){
console.log(data);

var icon = "http://openweathermap.org/img/w/" + data.weather[0].icon +".png";
var desc = data.weather[0].main;
var temperature = data.main.temp;

$('.icon').attr('src', icon);       //masukin ke class icon yg di html
$('.weather').append(desc);
$('.temp').append(temperature);
// console.log(icon +" cuacanya lg "+desc);
});


