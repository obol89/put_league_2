from flask import Flask, request, render_template, jsonify
import ast
import json
import backend

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    data = request.form.getlist('teams')
    data = data[0]
    data = ast.literal_eval(data)
    data.pop(0)
    print(data)
    return jsonify(result={"status": 200})

if __name__ == '__main__':
    app.run(debug=True)
