from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the SQLAlchemy database URI for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, nullable=False)
    page_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=True)


@app.route('/')
def inicio():
    logged_in = 'username' in session
    return render_template('index.html', logged_in=logged_in, current_user=session.get('username'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login validation (e.g., check credentials)
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'ax1':
            session['username'] = username
            return redirect(url_for('inicio'))

    return render_template('index.html', error='Invalid username or password')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('inicio'))


@app.route('/chapter/<int:chapter_id>/page/<int:page_id>', methods=['GET', 'POST'])
def chapter_page(chapter_id, page_id):
    page = Page.query.filter_by(chapter_id=chapter_id, page_id=page_id).first()

    if not page:
        return "404", 404

    logged_in = 'username' in session
    edit_mode = logged_in

    if request.method == 'POST':
        if logged_in and edit_mode:
            new_content = request.form.get('content')
            page.content = new_content
            db.session.commit()
        return redirect(url_for('chapter_page', chapter_id=chapter_id, page_id=page_id))

    return render_template('page.html', content=page.content, title=page.title, logged_in=logged_in,
                           edit_mode=edit_mode, current_chapter=chapter_id, current_page=page_id)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
