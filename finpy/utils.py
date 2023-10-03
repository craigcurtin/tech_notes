
def isMarketOpen():
  from datetime import datetime, timedelta
  import pandas_market_calendars as mcal

  previousday = datetime.now() - timedelta(5)
  nextday = datetime.now() + timedelta(5)
  nyse = mcal.get_calendar('NYSE')
  sched = nyse.schedule(start_date=previousday, end_date=nextday)

  return nyse.is_open_now(sched)


