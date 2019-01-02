from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight, height):
    height = height / 100
    bmi = round(weight / (height ** 2), 2)
    if bmi < 16:
        return "Your bmi is: " + str(bmi) + ". You are Several Underweight"
    elif bmi < 18.5:
        return "Your bmi is: " + str(bmi) + ". You are Underweight"
    elif bmi < 25:
        return "Your bmi is: " + str(bmi) + ". You are Normal"
    elif bmi < 30:
        return "Your bmi is: " + str(bmi) + ". You are Overweight"
    else:
        return "Your bmi is: " + str(bmi) + ". You are Obese"
  

if __name__ == '__main__':
  app.run(debug=True)