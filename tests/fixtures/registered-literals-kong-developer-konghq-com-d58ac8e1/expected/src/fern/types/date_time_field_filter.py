

import datetime as dt
import typing

from .date_time_field_filter_eq import DateTimeFieldFilterEq
from .date_time_field_filter_five import DateTimeFieldFilterFive
from .date_time_field_filter_four import DateTimeFieldFilterFour
from .date_time_field_filter_three import DateTimeFieldFilterThree
from .date_time_field_filter_two import DateTimeFieldFilterTwo

DateTimeFieldFilter = typing.Union[
    dt.datetime,
    DateTimeFieldFilterEq,
    DateTimeFieldFilterTwo,
    DateTimeFieldFilterThree,
    DateTimeFieldFilterFour,
    DateTimeFieldFilterFive,
]
