

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_tool_calls_code_output_image_object_image import (
    RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage,
)


class RunStepDeltaStepDetailsToolCallsCodeOutputImageObject(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    The index of the output in the outputs array.
    """

    image: typing.Optional[RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
