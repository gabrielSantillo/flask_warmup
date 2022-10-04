from flask import Flask
from dbhelpers import run_statement
import json

app = Flask(__name__)

@app.get('/api/books')
def get_all_books():
    results = run_statement("CALL get_all_books()")
    if(type(results) == list):
        books_json = json.dumps(results, default=str)
        return books_json
    else:
        return "Sorry, something has gone wrong."


@app.get('/api/books_authorized')
def get_all_books_authorized():
    results = run_statement("CALL books_written_by_author()")
    if(type(results) == list):
        books_authorized_json = json.dumps(results, default=str)
        return books_authorized_json
    else:
        return "Sorry, something has gone wrong."

@app.get('/api/best_selling_book')
def get_best_selling_books():
    results = run_statement("CALL most_copies_sold()")
    if(type(results) == list):
        best_selling_books_json = json.dumps(results, default=str)
        return best_selling_books_json
    else:
        return "Sorry, something has gone wrong."

@app.get('/api/best_selling_author')
def get_best_selling_author():
    results = run_statement("CALL most_sold_authors()")
    if(type(results) == list):
        best_selling_authors_json = json.dumps(results, default=str)
        return best_selling_authors_json
    else:
        return "Sorry, something has gone wrong."

app.run(debug=True)