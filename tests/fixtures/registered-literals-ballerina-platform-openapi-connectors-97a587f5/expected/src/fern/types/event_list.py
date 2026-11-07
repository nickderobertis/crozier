

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event import Event
from .type_discriminator import TypeDiscriminator


class EventList(UniversalBaseModel):
    """
    Represents a list of events.
    """

    object: typing.Optional[TypeDiscriminator] = None
    data: typing.Optional[typing.List[Event]] = pydantic.Field(default=None)
    """
    The list of items.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
