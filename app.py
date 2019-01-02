from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # router
def home(): # view function
    character = {
        "name": "AQUAMAN",
        "company": "DC COMICS",
        "image": "https://m.media-amazon.com/images/M/MV5BOTk5ODg0OTU5M15BMl5BanBnXkFtZTgwMDQ3MDY3NjM@._V1_.jpg",
        "abilities": ["Speed", "Strength", "Reflexs", "Underwater"]
    }

    return render_template("home.html", character=character)       # serve HTML               
@app.route("/c4e")
def c4e():
    return "Code For Everyone"

@app.route("/hi/<name>")
def say_hi(name):
    return "Hi " + name

@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    add = number1 + number2
    return str(add)




if __name__  == "__main__":
    app.run(debug=True)
