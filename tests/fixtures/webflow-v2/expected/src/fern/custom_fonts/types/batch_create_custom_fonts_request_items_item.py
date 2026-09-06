

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .batch_create_custom_fonts_request_items_item_axes_item import BatchCreateCustomFontsRequestItemsItemAxesItem
from .batch_create_custom_fonts_request_items_item_font_display import BatchCreateCustomFontsRequestItemsItemFontDisplay


class BatchCreateCustomFontsRequestItemsItem(UniversalBaseModel):
    file_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fileName"),
        pydantic.Field(
            alias="fileName",
            description="File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.",
        ),
    ]
    """
    File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.
    """

    file_hash: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fileHash"),
        pydantic.Field(
            alias="fileHash", description="Lowercase hex MD5 hash of the font binary (exactly 32 characters)"
        ),
    ]
    """
    Lowercase hex MD5 hash of the font binary (exactly 32 characters)
    """

    font_family: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fontFamily"),
        pydantic.Field(
            alias="fontFamily",
            description="The CSS font-family name (1-256 characters). Commas are stripped server-side.",
        ),
    ]
    """
    The CSS font-family name (1-256 characters). Commas are stripped server-side.
    """

    weight: int = pydantic.Field()
    """
    CSS font-weight value (1-1000)
    """

    italic: bool = pydantic.Field()
    """
    Whether the font is italic
    """

    font_display: typing_extensions.Annotated[
        BatchCreateCustomFontsRequestItemsItemFontDisplay,
        FieldMetadata(alias="fontDisplay"),
        pydantic.Field(alias="fontDisplay", description="CSS font-display value"),
    ]
    """
    CSS font-display value
    """

    axes: typing.Optional[typing.List[BatchCreateCustomFontsRequestItemsItemAxesItem]] = pydantic.Field(default=None)
    """
    Variable font axes. Omit or pass an empty array for static fonts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
