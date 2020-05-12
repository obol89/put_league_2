from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['team_name']
    processed_text = text.upper()


if __name__ == '_main__':
    app.run(debug=True)
