

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_security_group_network_type import LaunchLayerSecurityGroupNetworkType
from .launch_layer_security_group_type import LaunchLayerSecurityGroupType


class LaunchLayerSecurityGroup(UniversalBaseModel):
    """
    A security group LaunchLayer creates with the cluster and deletes with it.
    """

    name: str = pydantic.Field()
    """
    Security group name, referenced by node pools via securityGroupRefs.
    A DNS label of at most 24 characters, unique within the cluster.
    """

    type: LaunchLayerSecurityGroupType = pydantic.Field()
    """
    Immutable. A virtual VPC can contain both kinds of groups.
    """

    network_type: typing_extensions.Annotated[
        typing.Optional[LaunchLayerSecurityGroupNetworkType],
        FieldMetadata(alias="networkType"),
        pydantic.Field(
            alias="networkType", description="Required for a VIRTUALIZED group and rejected for a BARE_METAL group."
        ),
    ] = None
    """
    Required for a VIRTUALIZED group and rejected for a BARE_METAL group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
