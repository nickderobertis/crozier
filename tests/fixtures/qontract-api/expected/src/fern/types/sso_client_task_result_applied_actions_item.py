

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SsoClientTaskResultAppliedActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    auth_name: str
    cluster_name: str
    sso_client_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SsoClientTaskResultAppliedActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    sso_client_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SsoClientTaskResultAppliedActionsItem = typing_extensions.Annotated[
    typing.Union[SsoClientTaskResultAppliedActionsItem_Create, SsoClientTaskResultAppliedActionsItem_Delete],
    pydantic.Field(discriminator="action_type"),
]
