

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResponseStreamEvent_ResponseCreated(UniversalBaseModel):
    type: typing.Literal["response.created"] = "response.created"
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseStreamEvent_ResponseCompleted(UniversalBaseModel):
    type: typing.Literal["response.completed"] = "response.completed"
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResponseStreamEvent = typing_extensions.Annotated[
    typing.Union[ResponseStreamEvent_ResponseCreated, ResponseStreamEvent_ResponseCompleted],
    pydantic.Field(discriminator="type"),
]
