from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/preview")
def preview():
    import pandas
    
    df = pandas.read_csv('./train.csv')
    first_10_rwos = df.head(10).to_html(classes="table table-striped", index=False)
    return first_10_rwos

if __name__ == "__main__":
    app.run(debug=True)