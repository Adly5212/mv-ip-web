
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_data(site_name):
    conn = sqlite3.connect('sites_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT IP, LABEL, VLANID FROM sites WHERE SITE = ?", (site_name,))
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    site_name = ""
    if request.method == 'POST':
        site_name = request.form['site_name'].strip().upper()
        results = get_data(site_name)
    return render_template('index.html', results=results, site_name=site_name)

if __name__ == '__main__':
    app.run(debug=True)
