

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurveyEndingsItem_EndScreen(UniversalBaseModel):
    type: typing.Literal["endScreen"] = "endScreen"
    id: str
    headline: typing.Optional[typing.Dict[str, str]] = None
    subheader: typing.Optional[typing.Dict[str, str]] = None
    button_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="buttonLabel"), pydantic.Field(alias="buttonLabel")
    ] = None
    button_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="buttonLink"), pydantic.Field(alias="buttonLink")
    ] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SurveyEndingsItem_RedirectToUrl(UniversalBaseModel):
    type: typing.Literal["redirectToUrl"] = "redirectToUrl"
    id: str
    url: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SurveyEndingsItem = typing_extensions.Annotated[
    typing.Union[SurveyEndingsItem_EndScreen, SurveyEndingsItem_RedirectToUrl], pydantic.Field(discriminator="type")
]
