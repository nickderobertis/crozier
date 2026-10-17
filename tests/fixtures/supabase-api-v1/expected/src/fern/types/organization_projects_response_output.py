

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .organization_projects_response_output_pagination import OrganizationProjectsResponseOutputPagination
from .organization_projects_response_output_projects_item import OrganizationProjectsResponseOutputProjectsItem


class OrganizationProjectsResponseOutput(UniversalBaseModel):
    projects: typing.List[OrganizationProjectsResponseOutputProjectsItem]
    pagination: OrganizationProjectsResponseOutputPagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
