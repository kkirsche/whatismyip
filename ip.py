import socket

from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('VZIP_SETTINGS', silent=True)


@app.route('/')
def what_is_my_ip():
    return render_template('index.html', request=request)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
