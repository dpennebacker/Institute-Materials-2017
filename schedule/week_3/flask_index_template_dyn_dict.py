from flask import Flask
from flask import render_template
app = Flask(__name__)
values={'title': 'template index.html',
        'header': 'index.html',
        'paragraph': 'This is index.html with dynamic contents in response to a request for / (ROOT) in flask_index_template_dyn_dict.py'
}
@app.route("/")
def get_my_index():
     return render_template("index_dyn_dict.html", dict=values)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
