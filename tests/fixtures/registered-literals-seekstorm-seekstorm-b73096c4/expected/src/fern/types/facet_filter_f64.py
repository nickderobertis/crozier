

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_f64f64 import FacetFilterF64F64


class FacetFilterF64(UniversalBaseModel):
    """
    F64 range filter
    """

    f64: typing_extensions.Annotated[
        FacetFilterF64F64, FieldMetadata(alias="F64"), pydantic.Field(alias="F64", description="F64 range filter")
    ]
    """
    F64 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
