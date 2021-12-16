from flask import Flask, render_template
from . import main_bp

@main_bp.route("/")
def index_page():
    return render_template("index.html")