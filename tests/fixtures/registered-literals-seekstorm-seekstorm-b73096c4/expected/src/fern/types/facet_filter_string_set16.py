

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_string_set16string_set16 import FacetFilterStringSet16StringSet16


class FacetFilterStringSet16(UniversalBaseModel):
    """
    StringSet16 filter
    """

    string_set16: typing_extensions.Annotated[
        FacetFilterStringSet16StringSet16,
        FieldMetadata(alias="StringSet16"),
        pydantic.Field(alias="StringSet16", description="StringSet16 filter"),
    ]
    """
    StringSet16 filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
