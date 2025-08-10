from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html.j2")

import pandas
df = pandas.read_csv('./train.csv')

@app.route("/preview")
def preview():
    first_10_rwos = df.head(10).to_html(classes="table table-striped",bold_rows=True, index=False)
    return first_10_rwos

@app.route("/mean")
def mean():
    mean_of_age = df["Age"].mean()
    return f"<p>Mean Age: {mean_of_age:.2f}</p>"




if __name__ == "__main__":
    app.run(debug=True)