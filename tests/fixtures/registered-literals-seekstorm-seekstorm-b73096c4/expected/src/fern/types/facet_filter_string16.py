

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_string16string16 import FacetFilterString16String16


class FacetFilterString16(UniversalBaseModel):
    """
    String16 filter
    """

    string16: typing_extensions.Annotated[
        FacetFilterString16String16,
        FieldMetadata(alias="String16"),
        pydantic.Field(alias="String16", description="String16 filter"),
    ]
    """
    String16 filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
