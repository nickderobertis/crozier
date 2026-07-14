

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .serializer_types import SerializerTypes
from .transport_descriptor import TransportDescriptor


class TransportDependency(UniversalBaseModel):
    labels: typing.List[str] = pydantic.Field()
    """
    Set of labels that allow to define groups of transport bindings. The mechanism of the grouping is defined below this table.
    """

    serializers: typing.List[SerializerTypes] = pydantic.Field()
    """
    Information about the serializers in this transport binding, as defined in the SerializerTypes type in ETSI GS MEC 011 [i.4]. Support for at least one of the entries is required in conjunction with the transport.
    """

    transport: TransportDescriptor

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
