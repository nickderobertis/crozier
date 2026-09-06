

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompt_block_data_nullish import PromptBlockDataNullish
from .prompt_data_nullish_mcp_value import PromptDataNullishMcpValue
from .prompt_data_nullish_origin import PromptDataNullishOrigin
from .prompt_data_nullish_template_format import PromptDataNullishTemplateFormat
from .prompt_data_nullish_tool_functions_item import PromptDataNullishToolFunctionsItem
from .prompt_options_nullish import PromptOptionsNullish
from .prompt_parser_nullish import PromptParserNullish


class PromptDataNullish(UniversalBaseModel):
    """
    The prompt, model, and its parameters
    """

    prompt: typing.Optional[PromptBlockDataNullish] = None
    options: typing.Optional[PromptOptionsNullish] = None
    parser: typing.Optional[PromptParserNullish] = None
    tool_functions: typing.Optional[typing.List[PromptDataNullishToolFunctionsItem]] = None
    template_format: typing.Optional[PromptDataNullishTemplateFormat] = None
    mcp: typing.Optional[typing.Dict[str, typing.Optional[PromptDataNullishMcpValue]]] = None
    origin: typing.Optional[PromptDataNullishOrigin] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
