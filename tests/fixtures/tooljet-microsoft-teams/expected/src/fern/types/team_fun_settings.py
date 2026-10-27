

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .team_fun_settings_giphy_content_rating import TeamFunSettingsGiphyContentRating


class TeamFunSettings(UniversalBaseModel):
    allow_giphy: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowGiphy"), pydantic.Field(alias="allowGiphy")
    ] = None
    giphy_content_rating: typing_extensions.Annotated[
        typing.Optional[TeamFunSettingsGiphyContentRating],
        FieldMetadata(alias="giphyContentRating"),
        pydantic.Field(alias="giphyContentRating"),
    ] = None
    allow_stickers_and_memes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowStickersAndMemes"),
        pydantic.Field(alias="allowStickersAndMemes"),
    ] = None
    allow_custom_memes: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowCustomMemes"), pydantic.Field(alias="allowCustomMemes")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
