

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmGroupsTaskResultActionsItem_AddUserToGroup(UniversalBaseModel):
    action_type: typing.Literal["add_user_to_group"] = "add_user_to_group"
    cluster: str
    group: str
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OcmGroupsTaskResultActionsItem_DeleteUserFromGroup(UniversalBaseModel):
    action_type: typing.Literal["delete_user_from_group"] = "delete_user_from_group"
    cluster: str
    group: str
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


OcmGroupsTaskResultActionsItem = typing_extensions.Annotated[
    typing.Union[OcmGroupsTaskResultActionsItem_AddUserToGroup, OcmGroupsTaskResultActionsItem_DeleteUserFromGroup],
    pydantic.Field(discriminator="action_type"),
]
