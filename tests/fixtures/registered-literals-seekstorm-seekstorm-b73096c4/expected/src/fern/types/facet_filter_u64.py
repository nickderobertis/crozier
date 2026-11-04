

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_u64u64 import FacetFilterU64U64


class FacetFilterU64(UniversalBaseModel):
    """
    U64 range filter
    """

    u64: typing_extensions.Annotated[
        FacetFilterU64U64, FieldMetadata(alias="U64"), pydantic.Field(alias="U64", description="U64 range filter")
    ]
    """
    U64 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
