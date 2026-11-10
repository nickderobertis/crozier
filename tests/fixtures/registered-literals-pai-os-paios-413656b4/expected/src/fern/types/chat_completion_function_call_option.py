

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionFunctionCallOption(UniversalBaseModel):
    """
    Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.
    """

    name: str = pydantic.Field()
    """
    The name of the function to call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
