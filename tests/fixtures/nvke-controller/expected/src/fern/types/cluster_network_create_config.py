

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClusterNetworkCreateConfig(UniversalBaseModel):
    """
    Pod and service network. Immutable after creation. Defaults apply when omitted.
    """

    pod_cidr: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="podCIDR"),
        pydantic.Field(
            alias="podCIDR",
            description="Comma-separated IPv4 pod CIDRs. Each must be private, with a prefix length from\n/12 to /23, and must not overlap the others or the service CIDR. Must have room\nfor a /24 per desired node plus surge. Default 192.168.0.0/16.",
        ),
    ] = None
    """
    Comma-separated IPv4 pod CIDRs. Each must be private, with a prefix length from
    /12 to /23, and must not overlap the others or the service CIDR. Must have room
    for a /24 per desired node plus surge. Default 192.168.0.0/16.
    """

    service_cidr: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serviceCIDR"),
        pydantic.Field(
            alias="serviceCIDR", description="IPv4 service CIDR, private, /12 to /24. Default 10.96.0.0/12."
        ),
    ] = None
    """
    IPv4 service CIDR, private, /12 to /24. Default 10.96.0.0/12.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
