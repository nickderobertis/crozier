

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_u32u32 import FacetFilterU32U32


class FacetFilterU32(UniversalBaseModel):
    """
    U32 range filter
    """

    u32: typing_extensions.Annotated[
        FacetFilterU32U32, FieldMetadata(alias="U32"), pydantic.Field(alias="U32", description="U32 range filter")
    ]
    """
    U32 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
