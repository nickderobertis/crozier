

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    """
    Provides more information for an error status.
    """

    type: str = pydantic.Field()
    """
    The error type name.
    """

    summary: str = pydantic.Field()
    """
    Summary description of the error and causes.
    """

    traceback: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Stack trace leading to error (as a list of strings)
    """

    time: dt.datetime = pydantic.Field()
    """
    Time at which the error ocurred, to aid in log correlation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
