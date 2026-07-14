

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_description import EventDescription


class EventSubcategory(UniversalBaseModel):
    """
    A collection of events related to each other
    """

    description: typing.Optional[str] = None
    events: typing.Optional[typing.List[EventDescription]] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
