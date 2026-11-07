

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_string32string32 import FacetFilterString32String32


class FacetFilterString32(UniversalBaseModel):
    """
    String32 filter
    """

    string32: typing_extensions.Annotated[
        FacetFilterString32String32,
        FieldMetadata(alias="String32"),
        pydantic.Field(alias="String32", description="String32 filter"),
    ]
    """
    String32 filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
