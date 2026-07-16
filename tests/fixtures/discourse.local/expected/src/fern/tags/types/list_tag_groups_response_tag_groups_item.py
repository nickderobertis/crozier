

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_tag_groups_response_tag_groups_item_permissions import ListTagGroupsResponseTagGroupsItemPermissions


class ListTagGroupsResponseTagGroupsItem(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    one_per_topic: typing.Optional[bool] = None
    parent_tag_name: typing.Optional[typing.List[typing.Any]] = None
    permissions: typing.Optional[ListTagGroupsResponseTagGroupsItemPermissions] = None
    tag_names: typing.Optional[typing.List[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
