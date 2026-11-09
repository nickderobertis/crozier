

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistants_api_named_tool_choice_function import AssistantsApiNamedToolChoiceFunction
from .assistants_api_named_tool_choice_type import AssistantsApiNamedToolChoiceType


class AssistantsApiNamedToolChoice(UniversalBaseModel):
    """
    Specifies a tool the model should use. Use to force the model to call a specific tool.
    """

    type: AssistantsApiNamedToolChoiceType = pydantic.Field()
    """
    The type of the tool. If type is `function`, the function name must be set
    """

    function: typing.Optional[AssistantsApiNamedToolChoiceFunction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
