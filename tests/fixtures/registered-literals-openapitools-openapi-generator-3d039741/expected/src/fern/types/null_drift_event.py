

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .null_drift_response import NullDriftResponse


class NullDriftEvent_ResponseCompleted(UniversalBaseModel):
    type: typing.Literal["response.completed"] = "response.completed"
    response: NullDriftResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NullDriftEvent_Other(UniversalBaseModel):
    type: typing.Literal["other"] = "other"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


NullDriftEvent = typing_extensions.Annotated[
    typing.Union[NullDriftEvent_ResponseCompleted, NullDriftEvent_Other], pydantic.Field(discriminator="type")
]
