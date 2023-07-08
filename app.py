from flask import Flask, render_template, request, redirect, url_for
from models.user import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        user = User(username=username)
        user.save()

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/test', methods=['GET', 'POST'])
def test_user():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     user = User(username=username)
    #     user.save()

    #     return redirect(url_for('index'))

    return render_template('test.html')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    User.delete(user_id)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)
