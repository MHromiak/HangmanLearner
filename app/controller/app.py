from flask import Flask, render_template, redirect, url_for, request, abort


app = Flask(__name__)

key = ""

# _______Endpoints_______ #


@app.route('/main', methods = ['POST', 'GET'])
def main_screen():
    if request.form['mode'] == 'spanish':
        return redirect(url_for('spanish_categories'))
    elif request.form['mode'] == 'medical':
        return redirect(url_for('show_modes'))
    else:
        abort(406)

@app.route('/modes')
def show_modes():
    return 'Modes'


@app.route('/spanish')
def spanish_categories():
    return "Spanish here"


if __name__ == '__main__':
    app.run()

