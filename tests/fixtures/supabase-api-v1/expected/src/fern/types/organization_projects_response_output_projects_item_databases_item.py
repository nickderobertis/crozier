

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .organization_projects_response_output_projects_item_databases_item_disk_type import (
    OrganizationProjectsResponseOutputProjectsItemDatabasesItemDiskType,
)
from .organization_projects_response_output_projects_item_databases_item_infra_compute_size import (
    OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize,
)
from .organization_projects_response_output_projects_item_databases_item_status import (
    OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus,
)
from .organization_projects_response_output_projects_item_databases_item_type import (
    OrganizationProjectsResponseOutputProjectsItemDatabasesItemType,
)


class OrganizationProjectsResponseOutputProjectsItemDatabasesItem(UniversalBaseModel):
    infra_compute_size: typing.Optional[OrganizationProjectsResponseOutputProjectsItemDatabasesItemInfraComputeSize] = (
        None
    )
    region: str
    status: OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus
    cloud_provider: str
    identifier: str
    type: OrganizationProjectsResponseOutputProjectsItemDatabasesItemType
    disk_volume_size_gb: typing.Optional[float] = None
    disk_type: typing.Optional[OrganizationProjectsResponseOutputProjectsItemDatabasesItemDiskType] = None
    disk_throughput_mbps: typing.Optional[float] = None
    disk_last_modified_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
