

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool import Tool


class GenerateToolOutput(UniversalBaseModel):
    tool: Tool = pydantic.Field()
    """
    Generated tool
    """

    sample_args: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Sample arguments for the tool
    """

    response: str = pydantic.Field()
    """
    Response from the assistant
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
