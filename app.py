from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
app=Flask(__name__)
app.config[‘SECRET_KEY’]=”secret-phrase”
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False