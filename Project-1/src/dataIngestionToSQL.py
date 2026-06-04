import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv()

user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

df = pd.read_csv("employees.csv")

df.to_sql(
    "employees",
    engine,
    if_exists="append",
    index=False
)