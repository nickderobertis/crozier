

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_tool_calls_code_output_image_object_image import (
    RunStepDetailsToolCallsCodeOutputImageObjectImage,
)


class RunStepDetailsToolCallsCodeOutputImageObject(UniversalBaseModel):
    image: RunStepDetailsToolCallsCodeOutputImageObjectImage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
