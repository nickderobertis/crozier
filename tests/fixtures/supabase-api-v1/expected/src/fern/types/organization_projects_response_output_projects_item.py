

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .organization_projects_response_output_projects_item_databases_item import (
    OrganizationProjectsResponseOutputProjectsItemDatabasesItem,
)
from .organization_projects_response_output_projects_item_status import (
    OrganizationProjectsResponseOutputProjectsItemStatus,
)


class OrganizationProjectsResponseOutputProjectsItem(UniversalBaseModel):
    ref: str
    name: str
    cloud_provider: str
    region: str
    is_branch: bool
    status: OrganizationProjectsResponseOutputProjectsItemStatus
    inserted_at: str
    databases: typing.List[OrganizationProjectsResponseOutputProjectsItemDatabasesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
