import pandas as pd
from sqlalchemy import create_engine

# reads tabular data from a CSV file and converts into dataframe
df = pd.read_csv("employees.csv")


engine = create_engine(
    "mysql+pymysql://username:password@localhost/company_db"
)

df.to_sql(
    "employees",
    engine,
    if_exists="append",
    index=False
)