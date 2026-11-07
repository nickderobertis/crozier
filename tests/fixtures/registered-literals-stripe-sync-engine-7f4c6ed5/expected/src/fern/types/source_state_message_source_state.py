

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SourceStateMessageSourceState_Stream(UniversalBaseModel):
    state_type: typing.Literal["stream"] = "stream"
    stream: str
    data: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SourceStateMessageSourceState_Global(UniversalBaseModel):
    state_type: typing.Literal["global"] = "global"
    data: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SourceStateMessageSourceState = typing_extensions.Annotated[
    typing.Union[SourceStateMessageSourceState_Stream, SourceStateMessageSourceState_Global],
    pydantic.Field(discriminator="state_type"),
]
