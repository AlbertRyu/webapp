from flask import Flask

app = Flask(__name__)


@app.route("/")
def HelloWorld():
    return "<p>Hello World!</p>"


if __name__ == '__main__':
    # Run Flask on port 8080 (or any other port)
    app.run(port=8080)
