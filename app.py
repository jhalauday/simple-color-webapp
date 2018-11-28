import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

color_codes = {
	"red": "#e74c3c",
	"green": "#16a085",
	"blue": "#2980b9"
	}
	
color = os.environ.get('APP_COLOR') or random.choice("red","green","blue"])


@app.route("/")
def main():
    print(color)
	return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
	return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
