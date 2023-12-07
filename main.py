from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

DATABASE_URL = "postgresql://user:1@localhost/library"
"postgresql://username:password@host/db_name"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    created_at = Column(Date)

Base.metadata.create_all(bind=engine)

ItemPydantic = sqlalchemy_to_pydantic(Item, exclude=["id"])

db_item = ItemPydantic(title='War and Peace', author='L.Tolstoy', genre='Romain', created_at='1867-07-08')

def create_book(db_item:ItemPydantic):
    db_item = Item(**db_item.dict())
    with SessionLocal() as db:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    return db_item
create_book(db_item)
def get_book():
    result = []
    with SessionLocal() as db:
        items = db.query(Item).all()
        for item in items:
            result.append({'title': item.title, 'author': item.author, 'genre': item.genre, 'created_at': item.created_at})
    return result


def retrieve(item_id):
    with SessionLocal() as db:
        db_item = db.query(Item).filter(Item.id==item_id).first()
        
        if db_item is None:
            return None
        
        return {
            'title':db_item.title,
            'author':db_item.author,
            'genre':db_item.genre,
            'created_at':db_item.created_at
        }
def update_book(item_id:int, item:ItemPydantic):
    with SessionLocal() as db:
        db_item = db.query(Item).filter(Item.id==item_id).first()
        if db_item is None:
            return None
        
        for field, value in item.items():
            setattr(db_item, field, value)
        db.commit()
        db.refresh(db_item)
        return db_item

def delete_book(id:int):
    with SessionLocal() as db:
        db_item = db.query(Item).filter_by(id=id).first()

        if not db_item:
            return None
        
        db.delete(db_item)
        db.commit()
        return db_item
