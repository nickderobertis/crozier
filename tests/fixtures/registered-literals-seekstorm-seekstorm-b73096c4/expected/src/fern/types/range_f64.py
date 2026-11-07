

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RangeF64(UniversalBaseModel):
    """
    F64 range filter
    """

    start: float = pydantic.Field()
    """
    range start
    """

    end: float = pydantic.Field()
    """
    range end
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
