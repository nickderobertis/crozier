

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApplicationsDatapoint(UniversalBaseModel):
    count: typing.Optional[float] = pydantic.Field(default=None)
    """
    Count associated with timestamp
    """

    time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp for the related count.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
