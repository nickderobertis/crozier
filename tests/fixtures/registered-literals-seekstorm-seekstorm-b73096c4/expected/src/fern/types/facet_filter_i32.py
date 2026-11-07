

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_i32i32 import FacetFilterI32I32


class FacetFilterI32(UniversalBaseModel):
    """
    I32 range filter
    """

    i32: typing_extensions.Annotated[
        FacetFilterI32I32, FieldMetadata(alias="I32"), pydantic.Field(alias="I32", description="I32 range filter")
    ]
    """
    I32 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
