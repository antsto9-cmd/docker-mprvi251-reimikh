from flask import Flask, render_template

# The shared read-only volume contains the template used by both backends.
app = Flask(__name__, template_folder='/storage')


@app.route('/')
@app.route('/hello')
def hello_world():
    return render_template('index.html', source_app='app1')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
