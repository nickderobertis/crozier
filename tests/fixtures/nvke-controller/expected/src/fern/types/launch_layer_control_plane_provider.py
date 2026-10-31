

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_control_plane_provider_fulfillment_strategy import LaunchLayerControlPlaneProviderFulfillmentStrategy
from .launch_layer_security_group_refs import LaunchLayerSecurityGroupRefs
from .launch_layer_security_groups import LaunchLayerSecurityGroups


class LaunchLayerControlPlaneProvider(UniversalBaseModel):
    """
    LaunchLayer settings for the control-plane nodes. Same shape as
    LaunchLayerNodePoolProvider — control-plane nodes are still
    LaunchLayer machines. Fixed at creation.
    """

    instance_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="instanceType"),
        pydantic.Field(alias="instanceType", description='Requests capacity of a given shape, for example "vm200".'),
    ]
    """
    Requests capacity of a given shape, for example "vm200".
    """

    host_os_profile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hostOSProfile"),
        pydantic.Field(
            alias="hostOSProfile",
            description='Bare-metal profile, as "<name>" or "<name>:<version>". Mutually exclusive with vmProfile.',
        ),
    ] = None
    """
    Bare-metal profile, as "<name>" or "<name>:<version>". Mutually exclusive with vmProfile.
    """

    vm_profile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vmProfile"),
        pydantic.Field(
            alias="vmProfile",
            description='Virtual profile, as "<name>" or "<name>:<version>". Mutually exclusive with hostOSProfile.',
        ),
    ] = None
    """
    Virtual profile, as "<name>" or "<name>:<version>". Mutually exclusive with hostOSProfile.
    """

    fulfillment_strategy: typing_extensions.Annotated[
        typing.Optional[LaunchLayerControlPlaneProviderFulfillmentStrategy],
        FieldMetadata(alias="fulfillmentStrategy"),
        pydantic.Field(
            alias="fulfillmentStrategy", description="Controls how the Compute Allocation Operator places the request."
        ),
    ] = None
    """
    Controls how the Compute Allocation Operator places the request.
    """

    security_group_refs: typing_extensions.Annotated[
        typing.Optional[LaunchLayerSecurityGroupRefs],
        FieldMetadata(alias="securityGroupRefs"),
        pydantic.Field(alias="securityGroupRefs"),
    ] = None
    security_groups: typing_extensions.Annotated[
        typing.Optional[LaunchLayerSecurityGroups],
        FieldMetadata(alias="securityGroups"),
        pydantic.Field(alias="securityGroups"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
