from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Index")

@app.route('/tools')
def tools():
    return render_template('tools.html',
                           title="Tools")

def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
