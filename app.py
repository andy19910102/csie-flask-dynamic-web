from flask import Flask, render_template, request, session, redirect, url_for, flash
# TODO: 引用建立商品表單類別

app = Flask(__name__)

# TODO: 設定應用程式的SECRET_KEY


@app.route('/')
def index_page():
    # 首頁路由
    return render_template('index.html')


@app.route('/create_product')
def create_product_page():
    # 建立商品頁的路由
    # TODO: 建立商品表單的實例
    # TODO: 設定表單送出後的處理
    return render_template('create_product.html')


@app.route('/form_feedback')
def form_feedback():
    # 商品建立成功的路由
    return render_template('form_feedback.html')


if __name__ == '__main__':
    app.run(debug=True)
