

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmbeddingsListUsage(UniversalBaseModel):
    """
    Usage statistics for the model inference.
    """

    total_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of tokens consumed across all inputs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
