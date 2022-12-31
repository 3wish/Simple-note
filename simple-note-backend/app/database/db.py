from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:Hty023238@localhost/noteweb"
engine = create_engine(DATABASE_URL, echo=True)
