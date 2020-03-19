# 引用flask相關資源
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
# 引用時間模組
import time
import datetime
# TODO: 引用各種表單類別

# TODO: 初始化Firebase Firestore
# https://firebase.google.com/docs/firestore/quickstart

app = Flask(__name__)

# TODO: 設定應用程式的SECRET_KEY


@app.route('/')
def index_page():
    # TODO: 取得資料庫的商品列表資料
    # 首頁路由
    return render_template('index.html')


@app.route('/product/create')
def create_product_page():
    # 建立商品頁的路由

    # TODO: 建立商品表單的實例

    # TODO: 設定表單送出後的處理

    # TODO: 將新商品的資料儲存在session內以便下個頁面可顯示新資料
    return render_template('product/create.html')


@app.route('/product/create-finished')
def create_finished_page():
    # 商品建立成功的路由
    return render_template('product/create_finished.html')


@app.route('/product/<pid>/show')
def show_product_page():
    # 商品詳情頁的路由
    # TODO: 取得資料庫指定pid的商品資料
    return render_template('product/show.html')


@app.route('/product/<pid>/edit')
def edit_product_page():
    # 編輯商品頁的路由
    # TODO: 取得資料庫指定pid的商品資料
    # TODO: 建立編輯商品表單的實例
    # TODO: 建立刪除商品表單的實例
    return render_template('product/edit.html')


if __name__ == '__main__':
    # 應用程式開始運行
    app.run(debug=True)
