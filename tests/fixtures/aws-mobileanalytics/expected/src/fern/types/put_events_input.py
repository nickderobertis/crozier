

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event import Event


class PutEventsInput(UniversalBaseModel):
    """
    A container for the data needed for a PutEvent operation
    """

    events: typing.List[Event] = pydantic.Field()
    """
    An array of Event JSON objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
