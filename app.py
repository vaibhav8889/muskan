import handler
from flask import Flask, render_template
import logging

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/api/embed_url')
def home():
    embed_url = handler.get_embed_url()
    log.info(f"embed url: {embed_url}")
    embed_token = handler.get_access_token()
    log.info(f"embed token: {embed_token}")
    return render_template('index.html', embed_url=embed_url, embed_token=embed_token)

@app.route('/api/embed_url?<string:data>', methods=['GET'])
def api(data):
    embed_url = handler.get_embed_url(data)
    log.info(f"embed url: {embed_url}")
    embed_token = handler.get_access_token()
    log.info(f"embed token: {embed_token}")
    log.info(f"filter: {data}") 
    return render_template('index.html', embed_url=embed_url, embed_token=embed_token)

if __name__ == '__main__':
    app.run(debug=True)


