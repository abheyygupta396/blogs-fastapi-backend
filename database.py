
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:{}@localhost/blogs_database".format(quote_plus("AbheyGupta123@"))
SQLALCHEMY_DATABASE_URL = "postgresql://blogs_databse_user:xntcIqoFa9ufexJh4FGAe3wQKYuf91k9@dpg-cmuist6v3ddc738ivsgg-a.ohio-postgres.render.com/blogs_databse"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)