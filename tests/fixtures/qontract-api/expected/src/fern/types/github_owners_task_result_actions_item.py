

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GithubOwnersTaskResultActionsItem_AddOwner(UniversalBaseModel):
    action_type: typing.Literal["add_owner"] = "add_owner"
    org_name: str
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GithubOwnersTaskResultActionsItem = GithubOwnersTaskResultActionsItem_AddOwner
