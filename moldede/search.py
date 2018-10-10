import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import json

def searchPattern(pattern, type):
	with open('instance/catalogo.json') as f:
		data = json.load(f)
	result = []
	for film in data['films']:
		if pattern.lower() in film[type].lower():
			result.append(film)
	return result

def filter(pattern, type):
	with open('instance/catalogo.json') as f:
		data = json.load(f)
	result = []
	for film in data['films']:
		if pattern == str(film[type]):
			result.append(film)
	return result

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route("/pattern", methods=['POST'])
def search():
	if request.method == 'POST':
		pattern = request.form['pattern']
		message = "Results for " + pattern
		result = searchPattern(pattern, 'title')
		return render_template("index.html", message = message, pattern = pattern, films = result, number = len(result))

@bp.route("/categories", methods=['POST'])
def filterCategory():
	pattern = request.form['pattern']
	message = "Category: " + pattern
	result = searchPattern(pattern, 'category')
	return render_template("index.html", message = message, pattern = pattern, films = result, number = len(result))

@bp.route("/year", methods=['POST'])
def filterYear():
	pattern = request.form['pattern']
	message = "Films from " + pattern
	result = filter(pattern, 'year')
	return render_template("index.html", message = message, pattern = pattern, films = result, number = len(result))

@bp.route("/rating", methods=['POST'])
def filterRating():
	pattern = request.form['pattern']
	message = "Films rated " + pattern + "/5"
	result = filter(pattern, 'rating')
	return render_template("index.html", message = message,  pattern = pattern, films = result, number = len(result))
