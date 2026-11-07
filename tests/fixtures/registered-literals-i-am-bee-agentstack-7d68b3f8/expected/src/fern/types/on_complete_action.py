

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OnCompleteAction_AddProvider(UniversalBaseModel):
    type: typing.Literal["add_provider"] = "add_provider"
    auto_stop_timeout_sec: typing.Optional[int] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OnCompleteAction_UpdateProvider(UniversalBaseModel):
    type: typing.Literal["update_provider"] = "update_provider"
    provider_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OnCompleteAction_NoAction(UniversalBaseModel):
    type: typing.Literal["no_action"] = "no_action"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


OnCompleteAction = typing_extensions.Annotated[
    typing.Union[OnCompleteAction_AddProvider, OnCompleteAction_UpdateProvider, OnCompleteAction_NoAction],
    pydantic.Field(discriminator="type"),
]
