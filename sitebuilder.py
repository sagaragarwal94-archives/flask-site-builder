import sys

from flask import Flask, render_template
from flask_frozen import Freezer

DEBUG = True

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()

    else:
        app.run(port=8000)
