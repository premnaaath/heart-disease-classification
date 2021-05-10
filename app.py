from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('logistic_regression_model.pkl', 'rb'))


@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html', title='Home')


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        data = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        user_input = list()
        for i in data:
            x = request.form[i]
            if x == '':
                output = 1
                text = "Invalid Input!"
                return render_template('index.html', output=output, text=text)
            user_input.append(float(x))
        output = model.predict([user_input])
        if(output):
            text = "Your heart seems unhealthy, try to get it checked!"
            return render_template('index.html', output=output, text=text)
        else:
            text = "Your heart seems healthy!"
            return render_template("index.html", output=output, text=text)
    return render_template("index.html")


if(__name__ == '__main__'):
    app.run(debug=True)
