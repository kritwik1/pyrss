from flask import Flask, request, url_for, redirect
from flask import render_template
app=Flask(__name__)
@app.route("/")
def hello():
	return "Hello"
@app.route('/index')
def cool_form():
	return render_template('index.html')
@app.route('/rss')
def rss():
    return render_template('rss.xml')

if __name__=="__main__":
	app.debug=True
	app.run(host='0.0.0.0',port=80)
