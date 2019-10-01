# YOUR FLASK APP HERE
# Import Statements
from flask import Flask, render_template
from blueprints.operators import operators_blueprint
from blueprints.loops import loops_blueprint


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(loops_blueprint)
app.register_blueprint(operators_blueprint)

if __name__ == '__main__':
    app.run()