

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .a_notebook import ANotebook


class Action_CreateNotebook(UniversalBaseModel):
    type: typing.Literal["create-notebook"] = "create-notebook"
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_Join(UniversalBaseModel):
    type: typing.Literal["join"] = "join"
    ship: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_Leave(UniversalBaseModel):
    type: typing.Literal["leave"] = "leave"
    ship: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_AcceptInvite(UniversalBaseModel):
    type: typing.Literal["accept-invite"] = "accept-invite"
    ship: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_DeclineInvite(UniversalBaseModel):
    type: typing.Literal["decline-invite"] = "decline-invite"
    ship: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_Notebook(UniversalBaseModel):
    type: typing.Literal["notebook"] = "notebook"
    flag: str
    action: ANotebook

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_RegenerateApiKey(UniversalBaseModel):
    type: typing.Literal["regenerate-api-key"] = "regenerate-api-key"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Action_ClearApiKey(UniversalBaseModel):
    type: typing.Literal["clear-api-key"] = "clear-api-key"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Action = typing_extensions.Annotated[
    typing.Union[
        Action_CreateNotebook,
        Action_Join,
        Action_Leave,
        Action_AcceptInvite,
        Action_DeclineInvite,
        Action_Notebook,
        Action_RegenerateApiKey,
        Action_ClearApiKey,
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(Action_Notebook)
