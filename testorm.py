from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

# '''
# from testorm import engine
# from testorm import News
# News.metadata.create_all(engine)'''
engine = create_engine('mysql://root:@localhost:3306/newstest?charset=utf8')#连接
Base = declarative_base()#基类
Session = sessionmaker(bind=engine)

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable= False)
    content = Column(String(2000),nullable=False)
    news_types = Column(String(100),nullable=False)
    img_url = Column(String(200),)
    is_valid = Column(Boolean)
    view_count = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    author = Column(String(20),)

class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        #新增一条数据
       new_obj = News(
            title='标题',
            content='内容',
            news_types='百家',
        )
       # '''
       # new_obj = News(
       #     title='t',
       #     content='c',
       #     news_types= '1',
       # )'''
       self.session.add(new_obj)
       self.session.commit()
       return new_obj

    def get_one(self):
        #得到一条数据
        return  self.session.query(News).get(3)

    def get_more(self):
        #得到多条数据
        return self.session.query(News).filter_by(is_valid=False)

    def update_data(self,pk):
        # 更改一条
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return  True
        return  False

    def update_more(self):
        # 更改多条数据
        datalist = self.session.query(News).filter_by(is_valid=0)#filter可查区域例如大于5
        for item in datalist:
            item.is_valid = 1
            self.session.add(item)
        self.session.commit()

    def delete_data(self,pk):
        #删除一条
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            self.session.delete(new_obj)
            self.session.commit()

    def delete_more(self):
        #删除多条
        datalist = self.session.query(News).filter(News.id>3)#filter可查区域例如大于5
        for item in datalist:
            self.session.delete(item)
        self.session.commit()


if __name__ == '__main__':
    obj = OrmTest()
    rest = obj.add_one()
    print(rest.id)
    # rest = obj.get_more()
    # if rest:
    #     print(rest)
    #     #print('ID:{0}=>{1}'.format(rest.id,rest.title))
    # else:
    #     print('not exit.')
    # rest = obj.get_more()
    # print(rest.count())
    # for a in rest:
    #     print('ID:{0}=>{1}'.format(a.id, a.title))
    #print(obj.update_data(3))
    #print(obj.update_more())
    #obj.delete_data(1)
    #obj.delete_more()


