

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionStatus_Idle(UniversalBaseModel):
    type: typing.Literal["idle"] = "idle"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionStatus_Retry(UniversalBaseModel):
    type: typing.Literal["retry"] = "retry"
    attempt: float
    message: str
    next: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionStatus_Busy(UniversalBaseModel):
    type: typing.Literal["busy"] = "busy"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SessionStatus = typing_extensions.Annotated[
    typing.Union[SessionStatus_Idle, SessionStatus_Retry, SessionStatus_Busy], pydantic.Field(discriminator="type")
]
