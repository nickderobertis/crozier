

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolCallFunction(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the function to call
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    What the function does
    """

    arguments: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON object of arguments to pass to the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
