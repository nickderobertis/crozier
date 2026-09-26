

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .image_payload_images_item import ImagePayloadImagesItem
from .is_hidden import IsHidden


class ImagePayload(UniversalBaseModel):
    """
    Payload for IMAGE block type. Used for displaying images.
    """

    images: typing.Optional[typing.List[ImagePayloadImagesItem]] = None
    has_caption: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasCaption"),
        pydantic.Field(
            alias="hasCaption",
            description="Set to true to enable caption; caption must be present if hasCaption is true.",
        ),
    ] = None
    """
    Set to true to enable caption; caption must be present if hasCaption is true.
    """

    caption: typing.Optional[str] = pydantic.Field(default=None)
    """
    The caption text to display below the image.
    """

    has_link: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasLink"),
        pydantic.Field(
            alias="hasLink", description="Set to true to enable link; link must be present if hasLink is true."
        ),
    ] = None
    """
    Set to true to enable link; link must be present if hasLink is true.
    """

    link: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to link to when the image is clicked.
    """

    has_alt_text: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasAltText"),
        pydantic.Field(
            alias="hasAltText",
            description="Set to true to enable alt text; altText must be present if hasAltText is true.",
        ),
    ] = None
    """
    Set to true to enable alt text; altText must be present if hasAltText is true.
    """

    alt_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="altText"),
        pydantic.Field(alias="altText", description="The alternative text for the image."),
    ] = None
    """
    The alternative text for the image.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    column_list_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnListUuid], FieldMetadata(alias="columnListUuid"), pydantic.Field(alias="columnListUuid")
    ] = None
    column_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnUuid], FieldMetadata(alias="columnUuid"), pydantic.Field(alias="columnUuid")
    ] = None
    column_ratio: typing_extensions.Annotated[
        typing.Optional[ColumnRatio], FieldMetadata(alias="columnRatio"), pydantic.Field(alias="columnRatio")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
