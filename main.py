from flask import Flask, render_template, request

app = Flask(__name__)


# decorative

@app.route('/')
def home():
    return "Hello, World!"


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"


# @app.route('/add/<int:a>/<int:b>')
# def add(a,b):
#     return  f'result: {a+b}'

@app.route('/html')
def html():
    html = """
                  <h1>Hello world</h1>
                  <h3>hi there</h3>
                
           """
    return html


@app.route('/template')
def template():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def addition():
    result = None
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            result = a + b
        except (KeyError, ValueError):
            result = "Invalid input"
    return render_template('add.html', result=result)


@app.route('/simple', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            op = request.form['op']

            if op == 'add':
                result = a + b
            elif op == 'subtract':
                result = a - b
            elif op == 'multiply':
                result = a * b
            elif op == 'divide':
                if b != 0:
                    result = a / b
                else:
                    result = "Cannot divide by zero"
            else:
                result = "Invalid operations"

        except (KeyError, ValueError):
            result = "Invalid input"

    return render_template('simple.html', result=result)


@app.route('/bmi', methods=['GET', 'POST'])
def bmicalculate():
    result = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height_cm = float(request.form['height'])
            height_m = height_cm / 100

            if height_m > 0:
                bmi = weight / (height_m ** 2)
                result = round(bmi, 2)
            else:
                result = "Invalid height value"

        except (KeyError, ValueError):
            result = "Invalid input"

    return render_template('bmi.html', result=result)


@app.route('/area', methods=['GET', 'POST'])
def areacalculate():
    result = None
    if request.method == 'POST':
        try:
            shape = request.form['shape']

            if shape == 'triangle':
                base = float(request.form['base'])
                height = float(request.form['height'])
                result = 0.5 * base * height

            elif shape == 'rectangle':
                length = float(request.form['length'])
                width = float(request.form['width'])
                result = length * width

            elif shape == 'square':
                side = float(request.form['side'])
                result = side * side

            elif shape == 'circle':
                radius = float(request.form['radius'])
                result = 3.14159 * radius * radius

            else:
                result = "Invalid shape selected"

        except (KeyError, ValueError):
            result = "Invalid input"

    return render_template('area.html', result=result)


@app.route('/roller', methods=['GET', 'POST'])
def rollercoster():
    result = None
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            height = float(request.form['height'])
            weight = float(request.form['weight'])

            if age >= 12 and height >= 100 and weight >= 15:
                result = "You are allowed to ride the roller coaster!"
            else:
                result = "Sorry, you are not eligible for the roller coaster ride due to safety restrictions."

        except (KeyError, ValueError):
            result = "Invalid input. Please enter valid numbers."

    return render_template('roller.html', result=result)


@app.route('/loan', methods=['GET', 'POST'])
def loan():
    result = None
    if request.method == 'POST':
        try:
            P = float(request.form['amount'])
            R = float(request.form['rate']) / 1200
            N = int(request.form['years']) * 12

            if R == 0:
                emi = P / N
            else:
                emi = P * R * (1 + R) ** N / ((1 + R) ** N - 1)

            result = {
                'monthly_emi': round(emi, 2),
                'total_payment': round(emi * N, 2),
                'loan_amount': P,
                'interest_rate': float(request.form['rate']),
                'years': int(request.form['years'])
            }
        except:
            result = "Invalid input"
    return render_template('loan.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
