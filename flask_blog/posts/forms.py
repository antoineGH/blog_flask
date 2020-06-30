from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    excerpt = StringField('Excerpt', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Update Article Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')

class SearchForm(FlaskForm):
    search = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Search..."})
    filter = HiddenField('Filter')
