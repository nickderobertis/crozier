

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsGuardianRanksDestinyGuardianRankIconBackgroundsDefinition(UniversalBaseModel):
    background_empty_blue_gradient_bordered_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundEmptyBlueGradientBorderedImagePath")
    ] = None
    background_empty_bordered_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundEmptyBorderedImagePath")
    ] = None
    background_filled_blue_bordered_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledBlueBorderedImagePath")
    ] = None
    background_filled_blue_gradient_bordered_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledBlueGradientBorderedImagePath")
    ] = None
    background_filled_blue_low_alpha_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledBlueLowAlphaImagePath")
    ] = None
    background_filled_blue_medium_alpha_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledBlueMediumAlphaImagePath")
    ] = None
    background_filled_gray_heavy_alpha_bordered_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledGrayHeavyAlphaBorderedImagePath")
    ] = None
    background_filled_gray_medium_alpha_bordered_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledGrayMediumAlphaBorderedImagePath")
    ] = None
    background_filled_white_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledWhiteImagePath")
    ] = None
    background_filled_white_medium_alpha_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundFilledWhiteMediumAlphaImagePath")
    ] = None
    background_plate_black_alpha_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundPlateBlackAlphaImagePath")
    ] = None
    background_plate_black_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundPlateBlackImagePath")
    ] = None
    background_plate_white_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundPlateWhiteImagePath")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
