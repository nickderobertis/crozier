

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_tool_type import FunctionToolType


class FunctionTool(UniversalBaseModel):
    """
    Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).
    """

    type: FunctionToolType = pydantic.Field()
    """
    The type of the function tool. Always `function`.
    """

    name: str = pydantic.Field()
    """
    The name of the function to call.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the function. Used by the model to determine whether or not to call the function.
    """

    parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A JSON schema object describing the parameters of the function.
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enforce strict parameter validation. Default `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
