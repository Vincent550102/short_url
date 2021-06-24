from flask import Flask, render_template, request, redirect
from database import DataBase

app = Flask(__name__)
db = DataBase()

@app.route('/')
def index():
    ip = request.remote_addr
    # check AbuseIPDB
    return render_template('index.html', **locals())

@app.route('/web', methods=['POST'])
def web():
    #TODO
    ip = request.remote_addr
    url = request.values['url']
    code = db.allocatelCode()
    db.insert(code, url, ip)
    shorten_url = f"127.0.0.1/{code}"
    return render_template('fini.html', **locals())

@app.route("/<code>")
def api_info(code):
    ret = db.findByCode(code)
    if ret:
        return redirect(ret, code=302)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)