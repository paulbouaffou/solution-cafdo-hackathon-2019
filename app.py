#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Paul Bouaffou

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
		
	#return home page
	return render_template('index.html', title = "EducAid CI")

@app.route("/about")
def about():
		
	#return about page
	return render_template('about.html', title = "A propos | EducAid CI")

@app.route("/givedata")
def givedata():
		
	#return chart page
	return render_template('givedata.html', title = "Soumettre une donnee | EducAid CI")

@app.route("/result")
def result():
		
	#return chart page
	return render_template('result.html', title = "Donnee de l'Aide (IITA) | EducAid CI")

@app.route("/contact")
def contact():
		
	#return chart page
	return render_template('contact.html', title = "Nous contacter | EducAid CI")


@app.route("/needexprim")
def needexprim():
		
	#return chart page
	return render_template('needexprim.html', title = "Besoins exprimes | EducAid CI")

@app.route("/aidata")
def aidata():
		
	#return chart page
	return render_template('aidata.html', title = "Aide a l'Education | EducAid CI")

# Execute the application
if __name__ == '__main__':
	app.run()