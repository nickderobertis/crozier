

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_cluster_owner import LaunchLayerClusterOwner
from .launch_layer_cluster_provider_vpc_type import LaunchLayerClusterProviderVpcType
from .launch_layer_security_group import LaunchLayerSecurityGroup


class LaunchLayerClusterProvider(UniversalBaseModel):
    """
    LaunchLayer identifiers for the cluster. Exactly one of vpcID or orgID
    must be set, and siteID is required. All fields are fixed at creation.
    """

    vpc_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vpcID"),
        pydantic.Field(alias="vpcID", description="An existing LaunchLayer VPC that CAPLL observes but never deletes."),
    ] = None
    """
    An existing LaunchLayer VPC that CAPLL observes but never deletes.
    """

    org_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="orgID"),
        pydantic.Field(alias="orgID", description="Organization in which CAPLL creates a VPC when vpcID is omitted."),
    ] = None
    """
    Organization in which CAPLL creates a VPC when vpcID is omitted.
    """

    vpc_type: typing_extensions.Annotated[
        typing.Optional[LaunchLayerClusterProviderVpcType],
        FieldMetadata(alias="vpcType"),
        pydantic.Field(
            alias="vpcType",
            description="Network type for a managed or existing VPC. When omitted, CAPLL\ntreats the VPC as VIRTUALIZED. A VIRTUALIZED security group needs a\nVIRTUALIZED VPC.",
        ),
    ] = None
    """
    Network type for a managed or existing VPC. When omitted, CAPLL
    treats the VPC as VIRTUALIZED. A VIRTUALIZED security group needs a
    VIRTUALIZED VPC.
    """

    site_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="siteID"),
        pydantic.Field(alias="siteID", description="Names the LaunchLayer datahall this cluster's machines come from."),
    ]
    """
    Names the LaunchLayer datahall this cluster's machines come from.
    """

    cloud_provider_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="cloudProviderEnabled"),
        pydantic.Field(
            alias="cloudProviderEnabled",
            description="Set true where a cloud controller manager runs, so CAPLL leaves the\nNode's provider ID to it. NVKE runs no CCM, so true is rejected.",
        ),
    ] = None
    """
    Set true where a cloud controller manager runs, so CAPLL leaves the
    Node's provider ID to it. NVKE runs no CCM, so true is rejected.
    """

    owner: typing.Optional[LaunchLayerClusterOwner] = None
    security_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[LaunchLayerSecurityGroup]],
        FieldMetadata(alias="securityGroups"),
        pydantic.Field(
            alias="securityGroups", description="Security groups CAPLL creates with the cluster and deletes with it."
        ),
    ] = None
    """
    Security groups CAPLL creates with the cluster and deletes with it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
