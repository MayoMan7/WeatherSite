import bottle
import json
import data
import weather


@bottle.route("/")
def main_page():
  response = bottle.static_file("index.html", root=".")
  return response


@bottle.route("/script.js")
def script():
  response = bottle.static_file("script.js", root=".")
  return response


@bottle.route("/ajax.js")
def ajax():
  response = bottle.static_file("ajax.js", root=".")
  return response


@bottle.route("/style.css")
def style():
  response = bottle.static_file("style.css", root=".")
  return response


@bottle.route("/index.html")
def login_html():
  response = bottle.static_file("index.html", root=".")
  return response



@bottle.post("/main")
def main():
  response = json.loads(bottle.request.body.read().decode())
  print(response)
  return json.dumps(weather.get_weather(response))



bottle.run(host="0.0.0.0", port=8080)
