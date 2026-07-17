

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsSeasonsDestinySeasonPreviewImageDefinition(UniversalBaseModel):
    """
    Defines the thumbnail icon, high-res image, and video link for promotional images
    """

    high_res_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="highResImage"),
        pydantic.Field(
            alias="highResImage", description="An optional path to a high-resolution image, probably 1920x1080."
        ),
    ] = None
    """
    An optional path to a high-resolution image, probably 1920x1080.
    """

    thumbnail_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="thumbnailImage"),
        pydantic.Field(
            alias="thumbnailImage", description="A thumbnail icon path to preview seasonal content, probably 480x270."
        ),
    ] = None
    """
    A thumbnail icon path to preview seasonal content, probably 480x270.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
