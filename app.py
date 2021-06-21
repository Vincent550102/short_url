from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # some = "HELLO"
    return render_template('index.html', **locals())

@app.route('/web', methods=['POST'])
def web():
    #TODO
    shorten_url = "www.google.com"
    return render_template('fini.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)