

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .disk_selection_strategy_create import DiskSelectionStrategyCreate


class NicoNodePoolProvider(UniversalBaseModel):
    """
    NICo settings for a node pool. instanceTypeID and release are required,
    and exactly one of subnetIDs and vpcPrefixIDs is required.
    """

    subnet_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="subnetIDs"),
        pydantic.Field(alias="subnetIDs", description="Subnets, for sites without native networking."),
    ] = None
    """
    Subnets, for sites without native networking.
    """

    vpc_prefix_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="vpcPrefixIDs"),
        pydantic.Field(alias="vpcPrefixIDs", description="VPC prefixes, for sites with native networking."),
    ] = None
    """
    VPC prefixes, for sites with native networking.
    """

    instance_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="instanceTypeID"),
        pydantic.Field(alias="instanceTypeID", description="NICo instance type. Fixed at creation."),
    ] = None
    """
    NICo instance type. Fixed at creation.
    """

    infiniband_partition_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="infinibandPartitionID"),
        pydantic.Field(alias="infinibandPartitionID", description="InfiniBand partition. Fixed at creation."),
    ] = None
    """
    InfiniBand partition. Fixed at creation.
    """

    nv_link_logical_partition_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nvLinkLogicalPartitionID"),
        pydantic.Field(alias="nvLinkLogicalPartitionID", description="NVLink logical partition. Fixed at creation."),
    ] = None
    """
    NVLink logical partition. Fixed at creation.
    """

    ssh_key_group_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="sshKeyGroupIDs"),
        pydantic.Field(alias="sshKeyGroupIDs", description="SSH key groups for node access. Fixed at creation."),
    ] = None
    """
    SSH key groups for node access. Fixed at creation.
    """

    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of a release the Operator has supplied to the management plane.
    """

    disk_selection_strategy: typing_extensions.Annotated[
        typing.Optional[DiskSelectionStrategyCreate],
        FieldMetadata(alias="diskSelectionStrategy"),
        pydantic.Field(alias="diskSelectionStrategy"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
