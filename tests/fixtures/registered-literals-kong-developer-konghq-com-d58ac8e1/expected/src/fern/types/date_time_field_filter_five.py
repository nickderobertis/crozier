

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DateTimeFieldFilterFive(UniversalBaseModel):
    lte: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Value is greater than or equal to the given RFC-3339 formatted timestamp in UTC
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
