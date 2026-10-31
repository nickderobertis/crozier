

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LaunchLayerSecurityGroupRefs(UniversalBaseModel):
    """
    Names of the owning cluster's managed security groups to attach, per
    network interface. Mutually exclusive with securityGroups (existing
    group IDs) per interface.
    """

    primary_network_interface: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="primaryNetworkInterface"),
        pydantic.Field(
            alias="primaryNetworkInterface",
            description="Managed security group names to attach to the primary network interface.",
        ),
    ] = None
    """
    Managed security group names to attach to the primary network interface.
    """

    gpu_network_interface: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="gpuNetworkInterface"),
        pydantic.Field(
            alias="gpuNetworkInterface",
            description="Managed security group names to attach to the GPU network interface.",
        ),
    ] = None
    """
    Managed security group names to attach to the GPU network interface.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
