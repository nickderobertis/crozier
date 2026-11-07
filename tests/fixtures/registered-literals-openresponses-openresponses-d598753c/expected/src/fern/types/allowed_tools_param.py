

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .allowed_tools_param_mode import AllowedToolsParamMode
from .allowed_tools_param_type import AllowedToolsParamType
from .specific_tool_choice_param import SpecificToolChoiceParam


class AllowedToolsParam(UniversalBaseModel):
    type: AllowedToolsParamType = pydantic.Field()
    """
    The tool choice type. Always `allowed_tools`.
    """

    tools: typing.List[SpecificToolChoiceParam] = pydantic.Field()
    """
    The list of tools that are permitted for this request.
    """

    mode: typing.Optional[AllowedToolsParamMode] = pydantic.Field(default=None)
    """
    How to select a tool from the allowed set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
