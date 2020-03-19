from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput

category_options = [
    ('electronics', '電子產品類'),
    ('handmade', '手作類'),
    ('industrial', '工業類'),
    ('sports', '運動用品類'),
    ('outdoors', '戶外用品類'),
    ('toys', '玩具類'),
    ('others', '其他')
]


class CreateProductForm(FlaskForm):
    # TODO: 建立商品的表單
    # 名稱(title)
    title = StringField('產品標題', validators=[DataRequired()])
    # 縮圖網址(img_url)
    # 價格(price)
    # 是否銷售中(on_sale)
    # 類別(category)
    # 敘述(description)
    # 送出表單按鈕(submit)
    submit = SubmitField('建立商品')


class EditProductForm(FlaskForm):
    # TODO: 更新商品的表單
    # 名稱(title)
    title = StringField('產品標題', validators=[DataRequired()])
    # 縮圖網址(img_url)
    # 價格(price)
    # 是否銷售中(on_sale)
    # 類別(category[Electronics, Handmade, Industrial, Sports, Toys, Others])
    # 敘述(description)
    # 送出表單按鈕(submit)
    submit = SubmitField('更新商品')


class DeleteProductForm(FlaskForm):
    # 移除商品的表單
    # 確認刪除
    confirm = BooleanField('確認是否移除?', validators=[DataRequired()])
    # 送出按鈕
    submit = SubmitField('移除商品')


class CreateCommentForm(FlaskForm):
    # 新增留言的表單
    email = StringField('Email', validators=[DataRequired()])
    content = TextAreaField('留言內容', validators=[DataRequired()])
    submit = SubmitField('發佈留言')


class UpdateCommentForm(FlaskForm):
    # 更新留言的表單
    content = TextAreaField('留言內容', validators=[DataRequired()])
    submit = SubmitField('發佈留言')
