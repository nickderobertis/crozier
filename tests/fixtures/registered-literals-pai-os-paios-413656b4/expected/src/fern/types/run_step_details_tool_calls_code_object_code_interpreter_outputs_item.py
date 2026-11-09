

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_tool_calls_code_output_image_object_image import (
    RunStepDetailsToolCallsCodeOutputImageObjectImage,
)


class RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs(UniversalBaseModel):
    type: typing.Literal["logs"] = "logs"
    logs: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    image: RunStepDetailsToolCallsCodeOutputImageObjectImage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem = typing_extensions.Annotated[
    typing.Union[
        RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs,
        RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image,
    ],
    pydantic.Field(discriminator="type"),
]
