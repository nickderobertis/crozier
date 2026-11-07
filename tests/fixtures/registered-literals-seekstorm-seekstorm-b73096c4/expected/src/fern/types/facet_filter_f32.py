

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_f32f32 import FacetFilterF32F32


class FacetFilterF32(UniversalBaseModel):
    """
    F32 range filter
    """

    f32: typing_extensions.Annotated[
        FacetFilterF32F32, FieldMetadata(alias="F32"), pydantic.Field(alias="F32", description="F32 range filter")
    ]
    """
    F32 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
