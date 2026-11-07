

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_u8u8 import FacetFilterU8U8


class FacetFilterU8(UniversalBaseModel):
    """
    U8 range filter
    """

    u8: typing_extensions.Annotated[
        FacetFilterU8U8, FieldMetadata(alias="U8"), pydantic.Field(alias="U8", description="U8 range filter")
    ]
    """
    U8 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
