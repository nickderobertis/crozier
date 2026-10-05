

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ManagedSsoClientTaskResultAppliedActionsItem_Create(UniversalBaseModel):
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


class ManagedSsoClientTaskResultAppliedActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    client_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManagedSsoClientTaskResultAppliedActionsItem_MoveTenantSecret(UniversalBaseModel):
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


class ManagedSsoClientTaskResultAppliedActionsItem_Update(UniversalBaseModel):
    action_type: typing.Literal["update"] = "update"
    client_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ManagedSsoClientTaskResultAppliedActionsItem = typing_extensions.Annotated[
    typing.Union[
        ManagedSsoClientTaskResultAppliedActionsItem_Create,
        ManagedSsoClientTaskResultAppliedActionsItem_Delete,
        ManagedSsoClientTaskResultAppliedActionsItem_MoveTenantSecret,
        ManagedSsoClientTaskResultAppliedActionsItem_Update,
    ],
    pydantic.Field(discriminator="action_type"),
]
