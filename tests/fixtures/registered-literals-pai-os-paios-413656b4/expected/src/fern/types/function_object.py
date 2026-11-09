

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_parameters import FunctionParameters


class FunctionObject(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of what the function does, used by the model to choose when and how to call the function.
    """

    name: str = pydantic.Field()
    """
    The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    """

    parameters: typing.Optional[FunctionParameters] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
