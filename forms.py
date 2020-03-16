from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput


class CreateProductForm(FlaskForm):
    # TODO: 建立商品的表單
    # 名稱(title)
    # 縮圖網址(img_url)
    # 價格(price)
    # 是否銷售中(on_sale)
    # 類別(category[Electronics, Handmade, Industrial, Sports, Toys, Others])
    # 敘述(description)
    pass


class UpdateProductForm(FlaskForm):
    # TODO: 更新商品的表單
    # 名稱(title)
    # 縮圖網址(img_url)
    # 價格(price)
    # 是否銷售中(on_sale)
    # 類別(category[Electronics, Handmade, Industrial, Sports, Toys, Others])
    # 敘述(description)
    pass
