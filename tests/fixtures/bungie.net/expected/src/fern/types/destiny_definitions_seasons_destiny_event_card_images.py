

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsSeasonsDestinyEventCardImages(UniversalBaseModel):
    card_complete_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardCompleteImagePath")
    ] = None
    card_complete_wrap_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardCompleteWrapImagePath")
    ] = None
    card_incomplete_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardIncompleteImagePath")
    ] = None
    progress_icon_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="progressIconImagePath")
    ] = None
    theme_background_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="themeBackgroundImagePath")
    ] = None
    unowned_card_sleeve_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unownedCardSleeveImagePath")
    ] = None
    unowned_card_sleeve_wrap_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unownedCardSleeveWrapImagePath")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
