

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_groups_response_extras import ListGroupsResponseExtras
from .list_groups_response_groups_item import ListGroupsResponseGroupsItem


class ListGroupsResponse(UniversalBaseModel):
    extras: ListGroupsResponseExtras
    groups: typing.List[ListGroupsResponseGroupsItem]
    load_more_groups: str
    total_rows_groups: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
