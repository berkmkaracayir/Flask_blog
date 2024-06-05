from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'asfkjhdasfg4ljk4ad1hflkjash2lkaj'

DATABASE = 'database.db'

@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if not session.get('is_admin'):
        flash('Only admin users can access this page.')
        return redirect(url_for('index'))
    
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        is_admin = 1 if 'is_admin' in request.form else 0
        db.execute('UPDATE users SET username = ?, email = ?, is_admin = ? WHERE id = ?', (username, email, is_admin, id))
        db.commit()
        flash('User updated successfully.')
        return redirect(url_for('admin'))
    
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    if not session.get('is_admin'):
        flash('Only admin users can access this page.')
        return redirect(url_for('index'))
    
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (id,))
    db.commit()
    flash('User deleted successfully.')
    
    return redirect(url_for('admin'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if not session.get('user_id'):
        flash('Please log in to delete a post.')
        return redirect(url_for('login'))
    
    db = get_db()
    post = db.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    
    if post['user_id'] != session['user_id'] and not session.get('is_admin'):
        flash('You can only delete your own posts.')
        return redirect(url_for('index'))
    
    db.execute('DELETE FROM posts WHERE id = ?', (id,))
    db.commit()
    flash('Post deleted successfully.')
    
    return redirect(url_for('index'))

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM posts ORDER BY created DESC')
    posts = cur.fetchall()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    db = get_db()
    cur = db.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
    post = cur.fetchone()
    return render_template('post.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['is_admin'] = user['is_admin']
            session['username'] = user['username']
            if user['is_admin']:
                return redirect(url_for('admin'))
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        db = get_db()
        try:
            db.execute('INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, 0)', (username, email, hashed_password))
            db.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('is_admin', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if not session.get('user_id'):
        flash('Please log in to create a post.')
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']
        db = get_db()
        db.execute('INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
        db.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if not session.get('user_id'):
        flash('Please log in to edit a post.')
        return redirect(url_for('login'))
    
    db = get_db()
    post = db.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
    
    if post['user_id'] != session['user_id'] and not session.get('is_admin'):
        flash('You can only edit your own posts.')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
        db.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', post=post)

@app.route('/admin')
def admin():
    if not session.get('is_admin'):
        flash('Only admin users can access this page.')
        return redirect(url_for('index'))
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('admin.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
