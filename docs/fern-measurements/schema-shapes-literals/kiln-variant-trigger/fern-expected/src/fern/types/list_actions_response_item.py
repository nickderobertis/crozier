

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trigger import Trigger


class ListActionsResponseItem_Heat(UniversalBaseModel):
    kind: typing.Literal["heat"] = "heat"
    trigger: typing.Optional[Trigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ListActionsResponseItem_Cool(UniversalBaseModel):
    kind: typing.Literal["cool"] = "cool"
    trigger: typing.Optional[Trigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ListActionsResponseItem = typing_extensions.Annotated[
    typing.Union[ListActionsResponseItem_Heat, ListActionsResponseItem_Cool], pydantic.Field(discriminator="kind")
]
