

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_groups_response_user_groups_item import GetUserGroupsResponseUserGroupsItem


class GetUserGroupsResponse(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    user_groups: typing.Optional[typing.List[GetUserGroupsResponseUserGroupsItem]] = pydantic.Field(default=None)
    """
    A list of `user_group` objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
