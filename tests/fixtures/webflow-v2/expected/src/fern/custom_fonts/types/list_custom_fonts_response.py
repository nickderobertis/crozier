

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_custom_fonts_response_custom_fonts_item import ListCustomFontsResponseCustomFontsItem
from .list_custom_fonts_response_pagination import ListCustomFontsResponsePagination


class ListCustomFontsResponse(UniversalBaseModel):
    """
    A list of custom fonts
    """

    custom_fonts: typing_extensions.Annotated[
        typing.List[ListCustomFontsResponseCustomFontsItem],
        FieldMetadata(alias="customFonts"),
        pydantic.Field(alias="customFonts"),
    ]
    pagination: ListCustomFontsResponsePagination = pydantic.Field()
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
