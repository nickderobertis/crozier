

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmOidcIdpTaskResultActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    auth_name: str
    cluster_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OcmOidcIdpTaskResultActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    cluster_name: str
    idp_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OcmOidcIdpTaskResultActionsItem_Update(UniversalBaseModel):
    action_type: typing.Literal["update"] = "update"
    auth_name: str
    cluster_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


OcmOidcIdpTaskResultActionsItem = typing_extensions.Annotated[
    typing.Union[
        OcmOidcIdpTaskResultActionsItem_Create,
        OcmOidcIdpTaskResultActionsItem_Delete,
        OcmOidcIdpTaskResultActionsItem_Update,
    ],
    pydantic.Field(discriminator="action_type"),
]
