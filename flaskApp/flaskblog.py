from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
