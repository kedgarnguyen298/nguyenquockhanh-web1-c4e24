from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def user(username):
    users = {
        "khanh": {    
                "name": "Khánh",
                "gender": "male",
                "age": 19,
                "hobbies": "Code, movie, football",
                "avatar": "https://pickaface.net/gallery/avatar/Identical52046a933b5e3.png",
                },  
        "dung": {
                "username": "dung",
                "name": "Dung",
                "gender": "female",
                "age": 19,
                "hobbies": "Food, travel, movie",
                "avatar": "https://pickaface.net/gallery/avatar/41775795_180802_0453_xh4x3.png",
                }
    }
    
    return render_template("user.html", users=users, username=username)

  

if __name__ == '__main__':
  app.run(debug=True)