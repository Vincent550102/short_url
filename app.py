from flask import Flask, render_template, request, redirect, abort
from database import DataBase
import requests
import configparser
import json

app = Flask(__name__)
db = DataBase()


@app.route('/')
def index():
    config = configparser.ConfigParser()
    config.read('config.ini')
    ip = request.remote_addr
    domain = config['Domain']['domain']
    historys = db.findByAuthor(ip)
    
    return render_template('index.html', **locals())


@app.route('/web', methods=['POST'])
def web():
    # TODO
    ip = request.remote_addr
    # abuseipdb
    config = configparser.ConfigParser()
    config.read('config.ini')
    domain = config['Domain']['domain']
    abuseConfidenceScore = json.loads(requests.get(f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}', headers={
                                      'key': config['AbuseIPDB']['apikey']}).text)['data']['abuseConfidenceScore']
    if abuseConfidenceScore > 75:
        abort(403)
    url = request.values['url']
    code = db.allocatelCode(url, ip)
    shorten_url = f"{domain}/{code}"
    return render_template('fini.html', **locals())


@app.route("/<code>")
def api_info(code):
    url = db.findByCode(code)
    if url:
        db.codeClicked(code)
        return redirect(url, code=302)
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(403)
def forbidden(e):
    # note that we set the 404 status explicitly
    return render_template('403.html'), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
