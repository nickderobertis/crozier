

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_score import BaseScore


class NumericScore(BaseScore):
    value: float = pydantic.Field()
    """
    The numeric value of the score
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
