

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionBeginsPayload(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    Identifies the type of the message.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the streaming session.
    """

    expires_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp indicating when the session will expire.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
