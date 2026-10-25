

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .seconds import Seconds
from .symbols import Symbols


class RawMessage(UniversalBaseModel):
    """
    raw message seen on the bus.
    """

    master: Symbols = pydantic.Field()
    """
    the last seen master data bytes (only with raw and if available).
    """

    slave: typing.Optional[Symbols] = pydantic.Field(default=None)
    """
    the last seen slave data bytes (only with raw and if available).
    """

    lastup: typing.Optional[Seconds] = pydantic.Field(default=None)
    """
    the time in UTC seconds of the last update of the message (0 for never).
    """

    count: float = pydantic.Field()
    """
    number of times the master part was seen.
    """

    circuit: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the circuit in case of an already associated message definition.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the message in case of an already associated message definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
