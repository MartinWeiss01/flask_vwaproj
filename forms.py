from wtforms import Form, IntegerField, StringField, SelectField, PasswordField, validators

class SignInForm(Form):
    login = StringField(name='login', label='Login', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    password = PasswordField(name='password', label='Password', validators=[validators.Length(min=3), validators.InputRequired()])

class RegistrationUserForm(Form):
    firstname = StringField(name='firstname', label='First name', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    lastname = StringField(name='lastname', label='Last name', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    email = StringField('Email', validators=[validators.InputRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    password_repeat = PasswordField('Repeat password', validators=[validators.InputRequired(), validators.EqualTo('password')])
    phone = StringField('Phone number', validators=[validators.InputRequired(), validators.Regexp('^\+420\d{6}', message = 'Phone number must be starts on +420')])