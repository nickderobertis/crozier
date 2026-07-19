

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerateToolInput(UniversalBaseModel):
    tool_name: str = pydantic.Field()
    """
    Name of the tool to generate code for
    """

    prompt: str = pydantic.Field()
    """
    User prompt to generate code
    """

    handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Handle of the tool to generate code for
    """

    starter_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Python source code to parse for JSON schema
    """

    validation_errors: typing.List[str] = pydantic.Field()
    """
    List of validation errors
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
