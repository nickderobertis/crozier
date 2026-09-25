

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .location_location import LocationLocation
from .location_message_type import LocationMessageType


class Location(BaseMessageType):
    location: LocationLocation
    message_type: typing.Optional[LocationMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `location` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
