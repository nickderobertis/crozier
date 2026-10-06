

import typing

from .invalid_birthday_date import InvalidBirthdayDate
from .invalid_gender import InvalidGender

ErrorResultUnionInvalidGenderInvalidBirthdayDateData = typing.Union[InvalidGender, InvalidBirthdayDate]
