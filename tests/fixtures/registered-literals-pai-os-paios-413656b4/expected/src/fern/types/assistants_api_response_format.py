

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistants_api_response_format_type import AssistantsApiResponseFormatType


class AssistantsApiResponseFormat(UniversalBaseModel):
    """
    An object describing the expected output of the model. If `json_object` only `function` type `tools` are allowed to be passed to the Run. If `text` the model can return text or any value needed.
    """

    type: typing.Optional[AssistantsApiResponseFormatType] = pydantic.Field(default=None)
    """
    Must be one of `text` or `json_object`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
