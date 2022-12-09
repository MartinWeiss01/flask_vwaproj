from wtforms import Form, IntegerField, StringField, SelectField, PasswordField, validators



class SignInForm(Form):
    login = StringField(name='login', label='Login', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    password = PasswordField(name='password', label='Password', validators=[validators.Length(min=3), validators.InputRequired()])