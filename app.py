from flask import Flask, url_for, render_template, request, make_response

from markupsafe import escape

app = Flask(__name__)


@app.route('/hello/<name>')
@app.route("/hello")
def hello(name=None):
    if name is None:
        name = request.cookies.get('username')
    return render_template('hello.html', person=name)


@app.route("/")
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'Albert')
    return resp


@app.route("/about")
def About_page():
    return "<p style=font-family:Times New Roman;font-size:30pt> This is all about me! </p>"


@app.route("/<int:id>")
def id_page(id):
    return f"<p style=font-family:Times New Roman;font-size:30pt> {escape(id)} </p>"


with app.test_request_context():
    print(url_for('index'))
    #print(url_for('login'))
    #print(url_for('login', next='/'))
    #print(url_for('profile', username='Jahn Doe'))


if __name__ == '__main__':
    # Run Flask on port 8080 (or any other port)
    app.run(port=8080, debug=True)
