

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp_created import TimestampCreated
from .timestamp_destroyed import TimestampDestroyed
from .timestamp_updated import TimestampUpdated


class TimestampResConversation(UniversalBaseModel):
    created: typing.Optional[TimestampCreated] = None
    destroyed: typing.Optional[TimestampDestroyed] = None
    updated: typing.Optional[TimestampUpdated] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
