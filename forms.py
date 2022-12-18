from wtforms import Form, IntegerField, StringField, SelectField, PasswordField, validators



class SignInForm(Form):
    login = StringField(name='login', label='Login', validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    password = PasswordField(name='password', label='Password', validators=[validators.Length(min=3), validators.InputRequired()])





class RegistrationUserForm(Form):
    login = StringField(name='login', label='Login',
                        validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    username = StringField(name='login', label='Name',
                        validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    surname =  StringField(name='login', label='Surname',
                        validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    password = PasswordField('Password', validators=[validators.InputRequired()])

    password1 = PasswordField('Repeat password', validators=[validators.InputRequired(), validators.EqualTo('password')])

    email = StringField('Email', validators=[validators.InputRequired(), validators.Email()])

    phone = StringField('Phone number', validators=[validators.InputRequired(), validators.Regexp('^\+420\d{6}', message = 'Phone number must be starts on +420')])



