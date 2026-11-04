

import typing

from .after_date import AfterDate
from .before_date import BeforeDate

TimeRestriction = typing.Union[BeforeDate, AfterDate]
