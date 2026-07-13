

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConfigUserTheme(UniversalBaseModel):
    user_theme_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userThemeDescription")
    ] = None
    user_theme_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="userThemeId")] = None
    user_theme_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userThemeName")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
