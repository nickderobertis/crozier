

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SlackUsergroupActionUpdateUsersNotificationsItem_AddUser(UniversalBaseModel):
    action: typing.Literal["add-user"] = "add-user"
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SlackUsergroupActionUpdateUsersNotificationsItem_RemoveUser(UniversalBaseModel):
    action: typing.Literal["remove-user"] = "remove-user"
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SlackUsergroupActionUpdateUsersNotificationsItem = typing_extensions.Annotated[
    typing.Union[
        SlackUsergroupActionUpdateUsersNotificationsItem_AddUser,
        SlackUsergroupActionUpdateUsersNotificationsItem_RemoveUser,
    ],
    pydantic.Field(discriminator="action"),
]
