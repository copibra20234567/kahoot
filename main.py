from flask import *
from kpopfignya  import  *

app = Flask(__name__)
@app.route("/")
def index():
    sql= SQLManager("kahoot.db")
    quizzes = sql.select_quizzes()
    return render_template("index.html", quizzes = quizzes)

app.run(debug=True)
