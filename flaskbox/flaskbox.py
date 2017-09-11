from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello!"


def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
