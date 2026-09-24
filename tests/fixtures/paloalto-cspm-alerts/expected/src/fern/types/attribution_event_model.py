

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AttributionEventModel(UniversalBaseModel):
    """
    Model for AttributionEvent
    """

    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    Event
    """

    event_ts: typing.Optional[int] = pydantic.Field(default=None)
    """
    Event Timestamp
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Username
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
