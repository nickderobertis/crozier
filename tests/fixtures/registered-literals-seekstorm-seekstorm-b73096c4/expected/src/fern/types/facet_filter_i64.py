

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_i64i64 import FacetFilterI64I64


class FacetFilterI64(UniversalBaseModel):
    """
    I64 range filter
    """

    i64: typing_extensions.Annotated[
        FacetFilterI64I64, FieldMetadata(alias="I64"), pydantic.Field(alias="I64", description="I64 range filter")
    ]
    """
    I64 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
