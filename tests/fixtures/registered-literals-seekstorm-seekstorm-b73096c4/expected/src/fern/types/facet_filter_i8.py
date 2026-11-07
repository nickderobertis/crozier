

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_i8i8 import FacetFilterI8I8


class FacetFilterI8(UniversalBaseModel):
    """
    I8 range filter
    """

    i8: typing_extensions.Annotated[
        FacetFilterI8I8, FieldMetadata(alias="I8"), pydantic.Field(alias="I8", description="I8 range filter")
    ]
    """
    I8 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
