from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://Amol.Nikam:December%402665@localhost:5432/local_demo_db"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)