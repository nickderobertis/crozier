

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .range_u32 import RangeU32


class FacetFilterU32U32(UniversalBaseModel):
    """
    U32 range filter
    """

    field: str = pydantic.Field()
    """
    field name
    """

    filter: RangeU32 = pydantic.Field()
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
