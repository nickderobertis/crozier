

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ManagedSsoClientTaskResultActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    client_id: str
    tenant_secret_path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManagedSsoClientTaskResultActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    client_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManagedSsoClientTaskResultActionsItem_MoveTenantSecret(UniversalBaseModel):
    action_type: typing.Literal["move_tenant_secret"] = "move_tenant_secret"
    client_id: str
    tenant_secret_path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManagedSsoClientTaskResultActionsItem_Update(UniversalBaseModel):
    action_type: typing.Literal["update"] = "update"
    client_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ManagedSsoClientTaskResultActionsItem = typing_extensions.Annotated[
    typing.Union[
        ManagedSsoClientTaskResultActionsItem_Create,
        ManagedSsoClientTaskResultActionsItem_Delete,
        ManagedSsoClientTaskResultActionsItem_MoveTenantSecret,
        ManagedSsoClientTaskResultActionsItem_Update,
    ],
    pydantic.Field(discriminator="action_type"),
]
