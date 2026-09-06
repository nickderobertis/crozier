

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompt_block_data_nullish import PromptBlockDataNullish
from .prompt_data_mcp_value import PromptDataMcpValue
from .prompt_data_origin import PromptDataOrigin
from .prompt_data_template_format import PromptDataTemplateFormat
from .prompt_data_tool_functions_item import PromptDataToolFunctionsItem
from .prompt_options_nullish import PromptOptionsNullish
from .prompt_parser_nullish import PromptParserNullish


class PromptData(UniversalBaseModel):
    prompt: typing.Optional[PromptBlockDataNullish] = None
    options: typing.Optional[PromptOptionsNullish] = None
    parser: typing.Optional[PromptParserNullish] = None
    tool_functions: typing.Optional[typing.List[PromptDataToolFunctionsItem]] = None
    template_format: typing.Optional[PromptDataTemplateFormat] = None
    mcp: typing.Optional[typing.Dict[str, typing.Optional[PromptDataMcpValue]]] = None
    origin: typing.Optional[PromptDataOrigin] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
