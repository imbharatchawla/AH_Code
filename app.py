from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
        return render_template('index.html', name="CA Arika Hans")

app.run(host='0.0.0.0', port=8000, debug=True)
                             