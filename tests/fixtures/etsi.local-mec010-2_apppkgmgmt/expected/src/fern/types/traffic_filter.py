

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TrafficFilter(UniversalBaseModel):
    d_scp: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="dSCP")] = pydantic.Field(default=None)
    """
    Used to match all IPv4 packets that have the same DSCP.
    """

    dst_address: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="dstAddress")] = (
        pydantic.Field(default=None)
    )
    """
    A IP address or a range of IP addresses.For IPv4, the IP address could be an IP address plus mask, or an individual IP address, or a range of IP addresses.For IPv6, the IP address could be an IP prefix, or a range of IP prefixes.
    """

    dst_port: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="dstPort")] = (
        pydantic.Field(default=None)
    )
    """
    A port or a range of ports.
    """

    dst_tunnel_port: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="dstTunnelPort")
    ] = pydantic.Field(default=None)
    """
    Used for GTP tunnel based traffic rule.
    """

    protocol: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Specify the protocol of the traffic filter.
    """

    q_ci: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="qCI")] = pydantic.Field(default=None)
    """
    Used to match all packets that have the same QCI.
    """

    src_address: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="srcAddress")] = (
        pydantic.Field(default=None)
    )
    """
    An IP address or a range of IP addresses.For IPv4, the IP address could be an IP address plus mask, or an individual IP address, or a range of IP addresses.For IPv6, the IP address could be an IP prefix, or a range of IP prefixes.
    """

    src_port: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="srcPort")] = (
        pydantic.Field(default=None)
    )
    """
    A port or a range of ports.
    """

    src_tunnel_address: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="srcTunnelAddress")
    ] = pydantic.Field(default=None)
    """
    Used for GTP tunnel based traffic rule.
    """

    src_tunnel_port: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="srcTunnelPort")
    ] = pydantic.Field(default=None)
    """
    Used for GTP tunnel based traffic rule.
    """

    t_c: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="tC")] = pydantic.Field(default=None)
    """
    Used to match all IPv6 packets that have the same TC.
    """

    tag: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Used for tag based traffic rule.
    """

    tgt_tunnel_address: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="tgtTunnelAddress")
    ] = pydantic.Field(default=None)
    """
    Used for GTP tunnel based traffic rule.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
