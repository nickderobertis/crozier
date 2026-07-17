

import datetime as dt
import typing

NullableDateInterval = typing.Optional[typing.List[typing.Optional[dt.date]]]
"""
At least one entry should be non-null.
"""
