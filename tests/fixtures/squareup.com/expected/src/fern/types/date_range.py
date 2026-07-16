

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DateRange(UniversalBaseModel):
    """
    A range defined by two dates. Used for filtering a query for Connect v2
    objects that have date properties.
    """

    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string in `YYYY-MM-DD` format, such as `2017-10-31`, per the ISO 8601
    extended format for calendar dates.
    The end of a date range (inclusive).
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string in `YYYY-MM-DD` format, such as `2017-10-31`, per the ISO 8601
    extended format for calendar dates.
    The beginning of a date range (inclusive).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
