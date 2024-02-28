from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired(), Email()])
    subject = StringField("subject", validators=[DataRequired()])
    message = TextAreaField("message", validators=[DataRequired()])
