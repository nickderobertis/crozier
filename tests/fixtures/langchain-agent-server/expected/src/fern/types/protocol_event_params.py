

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .protocol_namespace import ProtocolNamespace


class ProtocolEventParams(UniversalBaseModel):
    namespace: ProtocolNamespace
    timestamp: int = pydantic.Field()
    """
    Wall-clock milliseconds since Unix epoch. Use `seq` for ordering.
    """

    data: typing.Any
    node: typing.Optional[str] = pydantic.Field(default=None)
    """
    Graph node that produced this event (messages, tools).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
