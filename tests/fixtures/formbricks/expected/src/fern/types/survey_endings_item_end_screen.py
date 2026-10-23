

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurveyEndingsItemEndScreen(UniversalBaseModel):
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
