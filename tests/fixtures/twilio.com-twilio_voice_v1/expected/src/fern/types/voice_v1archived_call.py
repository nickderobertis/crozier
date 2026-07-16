

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1ArchivedCall(UniversalBaseModel):
    date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The call sid
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
