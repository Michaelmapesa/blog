from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
import os


main=Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")