

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageSchedule(UniversalBaseModel):
    first_attempt: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time to make the first attempt for delivering the message. Must be RFC3339 format, in the future, and within 7 days of the request.
    """

    expires: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Expire and drop the message if not delivered by this time. Must be RFC3339 format, in the future, and within 8 days of the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
