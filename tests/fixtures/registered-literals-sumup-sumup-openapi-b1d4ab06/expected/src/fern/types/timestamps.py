

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Timestamps(UniversalBaseModel):
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the resource was created. This is a string as defined in [RFC 3339, section 5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the resource was last updated. This is a string as defined in [RFC 3339, section 5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
