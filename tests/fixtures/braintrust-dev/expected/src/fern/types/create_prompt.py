

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_type_enum_nullish import FunctionTypeEnumNullish
from .prompt_data_nullish import PromptDataNullish


class CreatePrompt(UniversalBaseModel):
    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the prompt belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the prompt
    """

    slug: str = pydantic.Field()
    """
    Unique identifier for the prompt
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the prompt
    """

    prompt_data: typing.Optional[PromptDataNullish] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags for the prompt
    """

    function_type: typing.Optional[FunctionTypeEnumNullish] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
