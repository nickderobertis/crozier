

import datetime as dt

ValueDateTime = dt.datetime
"""
Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry.
Usage: If transaction entry status is pending and value date is present, then the value date refers to an expected/requested value date.
For transaction entries subject to availability/float and for which availability information is provided, the value date must not be used. In this case the availability component identifies the number of availability days.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
All date-time fields in responses must include the timezone. An example is below:
2017-04-05T10:43:07+00:00
"""
