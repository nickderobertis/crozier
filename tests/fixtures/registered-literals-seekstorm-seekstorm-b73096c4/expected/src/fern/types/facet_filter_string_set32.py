

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_string_set32string_set32 import FacetFilterStringSet32StringSet32


class FacetFilterStringSet32(UniversalBaseModel):
    """
    StringSet32 filter
    """

    string_set32: typing_extensions.Annotated[
        FacetFilterStringSet32StringSet32,
        FieldMetadata(alias="StringSet32"),
        pydantic.Field(alias="StringSet32", description="StringSet32 filter"),
    ]
    """
    StringSet32 filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
