

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .abstract_exchange import AbstractExchange
from .event_message import EventMessage


class UnidirectionalEvent(AbstractExchange):
    """
    Representation of an unidirectional exchange as an event message
    """

    event_message: typing_extensions.Annotated[
        EventMessage,
        FieldMetadata(alias="eventMessage"),
        pydantic.Field(alias="eventMessage", description="Asynchronous message for this unidirectional event"),
    ]
    """
    Asynchronous message for this unidirectional event
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
