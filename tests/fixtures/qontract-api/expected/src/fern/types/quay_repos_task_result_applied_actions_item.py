

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuayReposTaskResultAppliedActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    description: str
    instance: str
    org_name: str
    public: bool
    repo_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayReposTaskResultAppliedActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    instance: str
    org_name: str
    repo_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayReposTaskResultAppliedActionsItem_UpdateDescription(UniversalBaseModel):
    action_type: typing.Literal["update_description"] = "update_description"
    description: str
    instance: str
    org_name: str
    repo_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayReposTaskResultAppliedActionsItem_UpdateVisibility(UniversalBaseModel):
    action_type: typing.Literal["update_visibility"] = "update_visibility"
    instance: str
    org_name: str
    public: bool
    repo_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


QuayReposTaskResultAppliedActionsItem = typing_extensions.Annotated[
    typing.Union[
        QuayReposTaskResultAppliedActionsItem_Create,
        QuayReposTaskResultAppliedActionsItem_Delete,
        QuayReposTaskResultAppliedActionsItem_UpdateDescription,
        QuayReposTaskResultAppliedActionsItem_UpdateVisibility,
    ],
    pydantic.Field(discriminator="action_type"),
]
