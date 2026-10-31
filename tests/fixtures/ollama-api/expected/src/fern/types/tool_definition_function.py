

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolDefinitionFunction(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Function name exposed to the model
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the function
    """

    parameters: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    JSON Schema for the function parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
