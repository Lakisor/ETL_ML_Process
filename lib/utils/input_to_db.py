import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://etl_user:etl_pass@localhost:5433/etl_db"
df = pd.read_csv("data/raw/input.csv")
engine = create_engine(DATABASE_URL)
df.to_sql("input_data", engine, if_exists="replace", index=False)
print("Done")
