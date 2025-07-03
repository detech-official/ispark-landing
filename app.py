from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home Page")

@app.route('/', subdomain='admin')
def admin_home():
    return render_template('admin_home.html')

if __name__ == '__main__':
    app.run(debug=True)