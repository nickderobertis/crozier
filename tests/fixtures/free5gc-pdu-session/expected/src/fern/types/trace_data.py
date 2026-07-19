

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ipv6addr import Ipv6Addr
from .trace_depth import TraceDepth


class TraceData(UniversalBaseModel):
    trace_ref: typing_extensions.Annotated[str, FieldMetadata(alias="traceRef"), pydantic.Field(alias="traceRef")]
    trace_depth: typing_extensions.Annotated[
        TraceDepth, FieldMetadata(alias="traceDepth"), pydantic.Field(alias="traceDepth")
    ]
    ne_type_list: typing_extensions.Annotated[
        str, FieldMetadata(alias="neTypeList"), pydantic.Field(alias="neTypeList")
    ]
    event_list: typing_extensions.Annotated[str, FieldMetadata(alias="eventList"), pydantic.Field(alias="eventList")]
    collection_entity_ipv4addr: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="collectionEntityIpv4Addr"),
        pydantic.Field(alias="collectionEntityIpv4Addr"),
    ] = None
    collection_entity_ipv6addr: typing_extensions.Annotated[
        typing.Optional[Ipv6Addr],
        FieldMetadata(alias="collectionEntityIpv6Addr"),
        pydantic.Field(alias="collectionEntityIpv6Addr"),
    ] = None
    interface_list: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="interfaceList"), pydantic.Field(alias="interfaceList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
