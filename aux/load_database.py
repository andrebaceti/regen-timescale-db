"""Create a dummy database just to simulate regen."""
import pandas as pd
import random
from sqlalchemy import create_engine


engine = create_engine(
    "postgresql://murabei:is_very_nice!@localhost/murabei")
pd.read_sql("SELECT 1;", con=engine)

###################
# Create database #
var1 = ["murabei", "is", "the", "nicest", "ds", "company"]

list_data = []
for id in range(1000):
    list_data.append({
        "id": id,
        "var": random.choice(var1),
        "value": random.normalvariate(0, 1)})

pd_list_data = pd.DataFrame(list_data)
pd_list_data.to_sql("data", con=engine, index=False)
