from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_username(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

#password validation for test purposes only 
def valid_login(username, password):
    return password == 'admin'

def log_the_user_in(username):
    return render_template('profile.html', username=username)

if __name__ == "__main__":
    app.run()
