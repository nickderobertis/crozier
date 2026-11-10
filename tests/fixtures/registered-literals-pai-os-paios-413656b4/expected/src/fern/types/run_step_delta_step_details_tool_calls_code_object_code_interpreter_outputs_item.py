

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_tool_calls_code_output_image_object_image import (
    RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage,
)


class RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs(UniversalBaseModel):
    type: typing.Literal["logs"] = "logs"
    index: int
    logs: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    index: int
    image: typing.Optional[RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem = typing_extensions.Annotated[
    typing.Union[
        RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs,
        RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image,
    ],
    pydantic.Field(discriminator="type"),
]
