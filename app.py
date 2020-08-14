from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///post.db'
db=SQLAlchemy(app)

class blog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    Blog_title=db.Column(db.String(100), nullable=False)
    Author=db.Column(db.String(100),nullable=False)
    Content=db.Column(db.Text, nullable=False)
    date_posted=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Post ' + str(self.id)

@app.route('/')
def default():
    return "<h1>This is Home Page<h1>"


@app.route('/home', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        new_post=blog(Blog_title=title,Author=author,Content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/home')
    else:
        all_post=blog.query.order_by(blog.date_posted).all()
        return render_template('index.html',posts=all_post)

@app.route('/home/delete/<int:id>')
def delete(id):
     post=blog.query.get_or_404(id)
     db.session.delete(post)
     db.session.commit()
     return redirect('/home')

@app.route('/home/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post=blog.query.get_or_404(id)
    if request.method == 'POST':
        post.Blog_title=request.form['e_title']
        post.Author=request.form['e_author']
        post.Content=request.form['e_content']
        db.session.commit()
        return redirect('/home')
    else:
        return render_template('edit.html',e_post=post)


if __name__=="__main__":
    app.run(debug=True)