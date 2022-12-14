from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# Created using pythons secrets module
app.config['SECRET_KEY'] = '4df5e137a01f8644319d422985f4fddb'

dummy = [
    {
        'title': 'Blog post 1',
        'author': 'Sikorosenai',
        'content': 'First post content',
        'date': 'December 12, 2022'
    }
]

# All return home
@app.route('/home')
@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', post=dummy)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
