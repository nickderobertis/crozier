

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_alias import ModelAlias


class Usage(UniversalBaseModel):
    """
    Token use of this answer, from the provider. Sent once, before `done`.
    """

    input_tokens: int
    output_tokens: int
    model: ModelAlias

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
