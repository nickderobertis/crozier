

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClusterNetwork(UniversalBaseModel):
    """
    Pod and service network in effect. Both fields are always present.
    """

    pod_cidr: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="podCIDR"),
        pydantic.Field(alias="podCIDR", description="Comma-separated IPv4 pod CIDRs in effect."),
    ]
    """
    Comma-separated IPv4 pod CIDRs in effect.
    """

    service_cidr: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceCIDR"),
        pydantic.Field(alias="serviceCIDR", description="IPv4 service CIDR in effect."),
    ]
    """
    IPv4 service CIDR in effect.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
