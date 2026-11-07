

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CitationsStylesReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the citation style entity.
    """

    date_parsed: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the citation style was first parsed, as an iso8601 formatted timestamp.
    """

    short_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short name for the citation style.
    """

    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    The summary of the citation style.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The official name of the citation style.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
