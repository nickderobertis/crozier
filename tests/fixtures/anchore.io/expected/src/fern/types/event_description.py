

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventDescription(UniversalBaseModel):
    """
    A description of an event type
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The message associated with the event type
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event type. The last component of the fully-qualified event_type (category.subcategory.event)
    """

    resource_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of resource this event is generated from
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fully qualified event type as would be seen in the event payload
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
