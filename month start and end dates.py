# -*- coding: utf-8 -*-

# import required modules
import pandas as pd
import calendar

# input start and end dates in YYYY-MM-DD format
start_date = '2000-01-01'
end_date = '2023-12-31'

# create a list of months in range in YYYY-MM format
pub_month = pd.date_range(start_date,end_date, 
              freq='MS').strftime("%Y-%m").tolist()

# create a list of month start dates in YYYY-MM-DD format
pub_month_start = pd.date_range(start_date,end_date, 
              freq='MS').strftime("%Y-%m-%d").tolist()

# create a list of month end dates in YYYY-MM-DD format
pub_month_end = []
for x in pub_month:
    year = int(x[0:4])
    month = int(x[5:7])
    num_days = calendar.monthrange(year,month)[1]
    month_end = x + "-" + str(num_days)
    pub_month_end.append(month_end)
    
# create a data frame by zipping the lists together and adding column headers
df = pd.DataFrame(list(zip(pub_month,pub_month_start,pub_month_end)),
                  columns = ['month','month_start','month_end'])