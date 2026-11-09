

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunToolCallObjectFunction(UniversalBaseModel):
    """
    The function definition.
    """

    name: str = pydantic.Field()
    """
    The name of the function.
    """

    arguments: str = pydantic.Field()
    """
    The arguments that the model expects you to pass to the function.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
