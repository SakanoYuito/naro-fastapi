from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import config

DB_URL = f'mysql+pymysql://{config.USERNAME}:{config.PASSWORD}@{config.HOSTNAME}:{config.PORT}/{config.DATABASE}'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()