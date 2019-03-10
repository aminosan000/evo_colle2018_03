# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

from dao import Dao

app = Flask(__name__)
dao = Dao()


@app.route('/', methods=['GET', 'POST'])
def top():
    if request.method == 'POST':
        input_values = {'name': request.form['name'],
                        'company': request.form['company'],
                        'tel': request.form['tel'],
                        'mail': request.form['mail']}
        dao.insert_business_card(input_values)

    registered = dao.select_all_business_cards()
    return render_template('index.html', registered=registered)


@app.route('/search', methods=['POST'])
def search():
    search_word = request.form['search_word']
    column = request.form['column']

    if column == 'name':
        registered = dao.select_business_cards_by_name(search_word)
    elif column == 'company':
        registered = dao.select_business_cards_by_company(search_word)
    elif column == 'tel':
        registered = dao.select_business_cards_by_tel(search_word)
    elif column == 'mail':
        registered = dao.select_business_cards_by_mail(search_word)
    else:
        registered = []

    return render_template('index.html', registered=registered)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
