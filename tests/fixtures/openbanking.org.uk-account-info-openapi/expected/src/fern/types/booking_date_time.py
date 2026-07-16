

import datetime as dt

BookingDateTime = dt.datetime
"""
Date and time when a transaction entry is posted to an account on the account servicer's books.
Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the actual booking date.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
All date-time fields in responses must include the timezone. An example is below:
2017-04-05T10:43:07+00:00
"""
