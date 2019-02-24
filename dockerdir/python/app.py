# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, request, session
from werkzeug.security import check_password_hash

from dao import Dao

app = Flask(__name__)
app.secret_key = 'this_is_secret_key'
dao = Dao()


# ページ遷移時にログイン判定
@app.before_request
def before_request():
    if session.get('user_id') or request.path == '/login':
        return

    return redirect('/login')


@app.route('/', methods=['GET', 'POST'])
def top():
    user_id = session.get('user_id')
    if request.method == 'POST':
        # 登録ボタンによって呼び出された場合、フォームの入力値をDBに登録
        values = {'name': request.form['name'],
                  'company': request.form['company'],
                  'tel': request.form['tel'],
                  'mail': request.form['mail'],
                  'user_id': user_id}
        dao.insert_business_card(values)

    # 登録済み情報を取得
    registered = dao.select_business_cards(user_id)
    return render_template('index.html', registered=registered)


@app.route('/login', methods=['GET', 'POST'])
def login():
    is_error = False
    if request.method == 'POST':
        # ログインボタンによって呼び出された場合、ログイン情報を照合
        user_id = request.form['user_id']
        password = request.form['password']

        user = dao.select_user(user_id)
        if user and check_password_hash(user.password, password):
            # ログイン成功
            session['user_id'] = user_id
            return redirect('/')
        is_error = True

    # 直接アクセス時、または認証失敗した場合、ログイン画面を表示
    return render_template('login.html', is_error=is_error)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
