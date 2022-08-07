from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass

    return render_template("index.html")
