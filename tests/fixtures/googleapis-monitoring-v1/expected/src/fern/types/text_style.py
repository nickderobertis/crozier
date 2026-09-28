

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .text_style_font_size import TextStyleFontSize
from .text_style_horizontal_alignment import TextStyleHorizontalAlignment
from .text_style_padding import TextStylePadding
from .text_style_pointer_location import TextStylePointerLocation
from .text_style_vertical_alignment import TextStyleVerticalAlignment


class TextStyle(UniversalBaseModel):
    """
    Properties that determine how the title and content are styled
    """

    background_color: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="backgroundColor"),
        pydantic.Field(
            alias="backgroundColor", description='The background color as a hex string. "#RRGGBB" or "#RGB"'
        ),
    ] = None
    """
    The background color as a hex string. "#RRGGBB" or "#RGB"
    """

    font_size: typing_extensions.Annotated[
        typing.Optional[TextStyleFontSize],
        FieldMetadata(alias="fontSize"),
        pydantic.Field(
            alias="fontSize",
            description="Font sizes for both the title and content. The title will still be larger relative to the content.",
        ),
    ] = None
    """
    Font sizes for both the title and content. The title will still be larger relative to the content.
    """

    horizontal_alignment: typing_extensions.Annotated[
        typing.Optional[TextStyleHorizontalAlignment],
        FieldMetadata(alias="horizontalAlignment"),
        pydantic.Field(
            alias="horizontalAlignment", description="The horizontal alignment of both the title and content"
        ),
    ] = None
    """
    The horizontal alignment of both the title and content
    """

    padding: typing.Optional[TextStylePadding] = pydantic.Field(default=None)
    """
    The amount of padding around the widget
    """

    pointer_location: typing_extensions.Annotated[
        typing.Optional[TextStylePointerLocation],
        FieldMetadata(alias="pointerLocation"),
        pydantic.Field(
            alias="pointerLocation", description='The pointer location for this widget (also sometimes called a "tail")'
        ),
    ] = None
    """
    The pointer location for this widget (also sometimes called a "tail")
    """

    text_color: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="textColor"),
        pydantic.Field(alias="textColor", description='The text color as a hex string. "#RRGGBB" or "#RGB"'),
    ] = None
    """
    The text color as a hex string. "#RRGGBB" or "#RGB"
    """

    vertical_alignment: typing_extensions.Annotated[
        typing.Optional[TextStyleVerticalAlignment],
        FieldMetadata(alias="verticalAlignment"),
        pydantic.Field(alias="verticalAlignment", description="The vertical alignment of both the title and content"),
    ] = None
    """
    The vertical alignment of both the title and content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
