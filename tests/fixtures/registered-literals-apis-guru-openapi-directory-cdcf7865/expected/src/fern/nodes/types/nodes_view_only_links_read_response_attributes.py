

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesViewOnlyLinksReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the view only link entity.
    """

    anonymous: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the view only link has anonymized contributors
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the view only link was created, as an iso8601 formatted timestamp.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The view only key
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the view only link
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
