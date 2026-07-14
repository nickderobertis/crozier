

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_tag_groups_response_tag_groups_item import ListTagGroupsResponseTagGroupsItem


class ListTagGroupsResponse(UniversalBaseModel):
    tag_groups: typing.Optional[typing.List[ListTagGroupsResponseTagGroupsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
