

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .range_u64 import RangeU64


class FacetFilterU64U64(UniversalBaseModel):
    """
    U64 range filter
    """

    field: str = pydantic.Field()
    """
    field name
    """

    filter: RangeU64 = pydantic.Field()
    """
    filter: range start, range end
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
