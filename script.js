function get_val() {
  let location = document.getElementById("loc").value;
  ajaxPostRequest("/main",JSON.stringify(location),temp);
}

function temp(inp) {
  let wet_dict = JSON.parse(inp);
  let location_data = wet_dict.location;
  let current_data = wet_dict.current;
  let condtion = current_data.condition;

  console.log(current_data);
  
  let name = location_data.name;
  let time = location_data.localtime;

  let temp = current_data.temp_f;
  let wind = current_data.wind_mph;
  let humidity = current_data.humidity;
  let uv = current_data.uv;
  let con = condtion.text;
  let con_icon = condtion.icon;
  

  let name_div = document.getElementById("name");
  name_div["innerHTML"] ="Location: " + name;

  let time_div = document.getElementById("time");
  time_div["innerHTML"] = "Time: " + time;

  let temp_div = document.getElementById("temp");
  temp_div["innerHTML"] = "Temp: " + temp + "°F";

  let wind_div = document.getElementById("wind");
  wind_div["innerHTML"] = "Wind: " + wind + " mph";

  let humidity_div = document.getElementById("humidity");
  humidity_div["innerHTML"] = "Humidity: " + humidity + "%";

  let uv_div = document.getElementById("uv");
  uv_div["innerHTML"] = "UV index: " + uv + "/10";

  let con_div = document.getElementById("con");
  con_div["innerHTML"] = "Condition: " + con;
 
  let con_icon_div = document.getElementById("con_icon");
  con_icon_div["src"] = con_icon;
}

