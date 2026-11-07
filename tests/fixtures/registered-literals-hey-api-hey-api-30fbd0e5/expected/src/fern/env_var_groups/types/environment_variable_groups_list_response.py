

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.pagination_links import PaginationLinks
from .environment_variable_groups_list_response_data_item import EnvironmentVariableGroupsListResponseDataItem


class EnvironmentVariableGroupsListResponse(UniversalBaseModel):
    """
    A paginated result set
    """

    data: typing.List[EnvironmentVariableGroupsListResponseDataItem]
    links: PaginationLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
