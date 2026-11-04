

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .range_f64 import RangeF64


class FacetFilterF64F64(UniversalBaseModel):
    """
    F64 range filter
    """

    field: str = pydantic.Field()
    """
    field name
    """

    filter: RangeF64 = pydantic.Field()
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
