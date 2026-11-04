

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_i16i16 import FacetFilterI16I16


class FacetFilterI16(UniversalBaseModel):
    """
    I16 range filter
    """

    i16: typing_extensions.Annotated[
        FacetFilterI16I16, FieldMetadata(alias="I16"), pydantic.Field(alias="I16", description="I16 range filter")
    ]
    """
    I16 range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
