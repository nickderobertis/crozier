

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PutV1TracesRequestItemTraceIp(UniversalBaseModel):
    nw_src: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source IP for IPv4.
    """

    nw_dst: typing.Optional[str] = pydantic.Field(default=None)
    """
    Destination IP for IPv4.
    """

    ipv6src: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ipv6_src"),
        pydantic.Field(alias="ipv6_src", description="Source IP for IPv6."),
    ] = None
    """
    Source IP for IPv6.
    """

    ipv6dst: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ipv6_dst"),
        pydantic.Field(alias="ipv6_dst", description="Destination IP for IPv6."),
    ] = None
    """
    Destination IP for IPv6.
    """

    nw_proto: typing.Optional[int] = pydantic.Field(default=None)
    """
    IP protocol
    """

    nw_tos: typing.Optional[int] = pydantic.Field(default=None)
    """
    IP TOS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
