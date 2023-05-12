from flask import Flask

app= Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, Protick"

if __name__== "__main__":
  print("I am in now")
  app.run(host='0.0.0.0', debug=True)