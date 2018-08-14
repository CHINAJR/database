from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/netnews?charset=utf8'
db = SQLAlchemy(app)

#终端先 from testflask import db     db.create_all()创建表
class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable= False)
    content = db.Column(db.String(2000),nullable=False)
    news_types = db.Column(db.String(100),nullable=False)
    img_url = db.Column(db.String(200),)
    is_valid = db.Column(db.Boolean)
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    author = db.Column(db.String(20),)

    # def __repr__(self):
    #     return '<News %r>'%self.title

@app.route('/')
# def hello_world():
#     return 'hello world hell'
def index():
    news_list = News.query.all()
    #print(news_list)
    return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>/')
def cat(name):
    '''新闻类别'''
    #查询类别name的新闻数据
    news_list = News.query.filter(News.news_types == name)
    return render_template('cat.html',name=name,news_list=news_list)

@app.route('/detail/<int:pk>/')
def detail(pk):
    new_obj = News.query.get(pk)
    return  render_template('detail.html', new_obj=new_obj)

if __name__ == '__main__':
    app.run(debug=True)
