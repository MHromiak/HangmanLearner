from flask import Flask, render_template, redirect, url_for, request, abort
import os


template_dir = os.path.abspath('../view/templates')
app = Flask(__name__, template_folder=template_dir)

key = ""

# _______Endpoints_______ #


@app.route('/main', methods=['POST', 'GET'])
def main_screen():
    return render_template("main.html")


@app.route('/modes')
def show_modes():
    return 'Modes'


@app.route('/spanish')
def spanish_categories():
    return "Spanish here"


if __name__ == '__main__':
    app.run()

