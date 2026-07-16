

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsSeasonsDestinyEventCardImages(UniversalBaseModel):
    card_complete_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cardCompleteImagePath"),
        pydantic.Field(alias="cardCompleteImagePath"),
    ] = None
    card_complete_wrap_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cardCompleteWrapImagePath"),
        pydantic.Field(alias="cardCompleteWrapImagePath"),
    ] = None
    card_incomplete_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cardIncompleteImagePath"),
        pydantic.Field(alias="cardIncompleteImagePath"),
    ] = None
    progress_icon_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="progressIconImagePath"),
        pydantic.Field(alias="progressIconImagePath"),
    ] = None
    theme_background_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="themeBackgroundImagePath"),
        pydantic.Field(alias="themeBackgroundImagePath"),
    ] = None
    unowned_card_sleeve_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unownedCardSleeveImagePath"),
        pydantic.Field(alias="unownedCardSleeveImagePath"),
    ] = None
    unowned_card_sleeve_wrap_image_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unownedCardSleeveWrapImagePath"),
        pydantic.Field(alias="unownedCardSleeveWrapImagePath"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
