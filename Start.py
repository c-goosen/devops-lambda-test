import json
import dateutil.relativedelta
from datetime import date, datetime , timedelta

def handler_func(event, context):
    start_date = date.today() 
    end_date = start_date+dateutil.relativedelta.relativedelta(days=7)
    delta = timedelta(days=1)
    date_range = []
    while start_date <= end_date:
        date_range.append(start_date.strftime("%Y-%m-%d"))
        start_date += delta
    
    return {
        "statusCode": 200,
        "body": json.dumps(date_range)
    }
