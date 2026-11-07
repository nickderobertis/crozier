

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_u16u16 import FacetFilterU16U16


class FacetFilterU16(UniversalBaseModel):
    """
    U16 range filter
    """

    u16: typing_extensions.Annotated[
        FacetFilterU16U16, FieldMetadata(alias="U16"), pydantic.Field(alias="U16", description="U16 range filter")
    ]
    """
    U16 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
