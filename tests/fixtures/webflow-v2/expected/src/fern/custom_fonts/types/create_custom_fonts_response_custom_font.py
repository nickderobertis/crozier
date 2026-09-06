

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_custom_fonts_response_custom_font_axes_item import CreateCustomFontsResponseCustomFontAxesItem
from .create_custom_fonts_response_custom_font_font_display import CreateCustomFontsResponseCustomFontFontDisplay
from .create_custom_fonts_response_custom_font_format import CreateCustomFontsResponseCustomFontFormat


class CreateCustomFontsResponseCustomFont(UniversalBaseModel):
    """
    A custom font uploaded to a Webflow site
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the custom font
    """

    font_family: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fontFamily"),
        pydantic.Field(alias="fontFamily", description="The CSS font-family name. Commas are stripped server-side."),
    ]
    """
    The CSS font-family name. Commas are stripped server-side.
    """

    format: typing.Optional[CreateCustomFontsResponseCustomFontFormat] = pydantic.Field(default=None)
    """
    The font file format, derived from the file extension. The value `svg` represents read-only legacy data; new SVG font uploads are not accepted.
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="The file name supplied at upload time"),
    ] = None
    """
    The file name supplied at upload time
    """

    weight: int = pydantic.Field()
    """
    The CSS font-weight value (1–1000)
    """

    italic: bool = pydantic.Field()
    """
    Whether the font is italic
    """

    font_display: typing_extensions.Annotated[
        CreateCustomFontsResponseCustomFontFontDisplay,
        FieldMetadata(alias="fontDisplay"),
        pydantic.Field(alias="fontDisplay", description="The CSS font-display value"),
    ]
    """
    The CSS font-display value
    """

    axes: typing.List[CreateCustomFontsResponseCustomFontAxesItem] = pydantic.Field()
    """
    Variable font axes. An empty array indicates a static font.
    """

    hosted_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hostedUrl"),
        pydantic.Field(alias="hostedUrl", description="CDN URL for the font binary"),
    ] = None
    """
    CDN URL for the font binary
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
