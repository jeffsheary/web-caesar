from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return render_template('about.html')

#instead of returning to about.html, could return to a second index.html that
#will display it under the thing that looks the exact same as this page, instead
#of a the about page

@app.route('/home/about', methods=['POST'])
def about():
    rot_amount = request.form.get("rotation-amount")
    new_text = request.form.get("block-text")
    ## TODO:
    # run caesar algorithm
    # receive a list/string/whatever you want with the answer
    return render_template('about.html', rot = rot_amount, b_text = new_text)

app.run(debug = True)

