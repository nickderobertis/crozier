

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LaunchLayerSecurityGroups(UniversalBaseModel):
    """
    Existing LaunchLayer security group IDs to attach, per network interface.
    Mutually exclusive with securityGroupRefs on the same interface. These
    groups remain externally managed and are not deleted with the cluster.
    """

    primary_network_interface: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="primaryNetworkInterface"),
        pydantic.Field(
            alias="primaryNetworkInterface",
            description="Existing security group IDs to attach to the primary network interface.",
        ),
    ] = None
    """
    Existing security group IDs to attach to the primary network interface.
    """

    gpu_network_interface: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="gpuNetworkInterface"),
        pydantic.Field(
            alias="gpuNetworkInterface",
            description="Existing security group IDs to attach to the GPU network interface.",
        ),
    ] = None
    """
    Existing security group IDs to attach to the GPU network interface.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
