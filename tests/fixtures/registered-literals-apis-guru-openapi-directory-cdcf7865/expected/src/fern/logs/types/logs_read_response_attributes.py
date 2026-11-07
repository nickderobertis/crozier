

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logs_read_response_attributes_params import LogsReadResponseAttributesParams


class LogsReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the log.
    """

    action: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of action performed on the OSF. See actions section for full list of possible actions.
    """

    date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time at which the log was created, as an iso8601 formatted timestamp.
    """

    params: typing.Optional[LogsReadResponseAttributesParams] = pydantic.Field(default=None)
    """
    The type of action performed on the OSF. See description for full list of possible actions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
