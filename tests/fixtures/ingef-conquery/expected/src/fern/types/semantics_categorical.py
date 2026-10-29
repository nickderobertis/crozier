

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .semantics_base import SemanticsBase


class SemanticsCategorical(SemanticsBase):
    """
    Values are an enumeration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
