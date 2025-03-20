import datetime
import random
import pandas as pd

y2024_first_day = datetime.date(2024, 1, 1)
y2025_first_day = datetime.date(2025, 1, 1)
interval = y2025_first_day - y2024_first_day
y2024_all = [y2024_first_day + datetime.timedelta(days=x) for x in range(interval.days)]
values = [random.random() for _ in range(interval.days)]

pd.DataFrame(data={
    "date": y2024_all,
    "value": values,
}).to_parquet("dummy.parquet")