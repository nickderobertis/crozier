

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_name import AppName
from .auth_configuration import AuthConfiguration


class AppConfig(UniversalBaseModel):
    auth_configuration: typing_extensions.Annotated[
        AuthConfiguration, FieldMetadata(alias="authConfiguration"), pydantic.Field(alias="authConfiguration")
    ]
    app_name: typing_extensions.Annotated[AppName, FieldMetadata(alias="appName"), pydantic.Field(alias="appName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
