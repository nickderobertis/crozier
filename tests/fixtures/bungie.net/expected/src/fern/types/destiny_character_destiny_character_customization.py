

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyCharacterDestinyCharacterCustomization(UniversalBaseModel):
    """
    Raw data about the customization options chosen for a character's face and appearance.
    You can look up the relevant class/race/gender combo in DestinyCharacterCustomizationOptionDefinition for the character, and then look up these values within the CustomizationOptions found to pull some data about their choices. Warning: not all of that data is meaningful. Some data has useful icons. Others have nothing, and are only meant for 3D rendering purposes (which we sadly do not expose yet)
    """

    decal_color: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="decalColor"), pydantic.Field(alias="decalColor")
    ] = None
    decal_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="decalIndex"), pydantic.Field(alias="decalIndex")
    ] = None
    eye_color: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="eyeColor"), pydantic.Field(alias="eyeColor")
    ] = None
    face: typing.Optional[int] = None
    feature_colors: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="featureColors"), pydantic.Field(alias="featureColors")
    ] = None
    feature_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="featureIndex"), pydantic.Field(alias="featureIndex")
    ] = None
    hair_colors: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="hairColors"), pydantic.Field(alias="hairColors")
    ] = None
    hair_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="hairIndex"), pydantic.Field(alias="hairIndex")
    ] = None
    lip_color: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lipColor"), pydantic.Field(alias="lipColor")
    ] = None
    personality: typing.Optional[int] = None
    skin_color: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="skinColor"), pydantic.Field(alias="skinColor")
    ] = None
    wear_helmet: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="wearHelmet"), pydantic.Field(alias="wearHelmet")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
