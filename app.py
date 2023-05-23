from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, nullable=False)
    page_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=True)


@app.route('/chapter/<int:chapter_id>/page/<int:page_id>')
def chapter_page(chapter_id, page_id):
    page = Page.query.filter_by(chapter_id=chapter_id, page_id=page_id).first()

    if not page:
        return "404", 404

    return render_template('page.html', content=page.content, title=page.title , current_chapter=chapter_id, current_page=page_id)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
