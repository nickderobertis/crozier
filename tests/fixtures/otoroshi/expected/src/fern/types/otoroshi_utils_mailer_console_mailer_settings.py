

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_utils_mailer_console_mailer_settings_type import OtoroshiUtilsMailerConsoleMailerSettingsType


class OtoroshiUtilsMailerConsoleMailerSettings(UniversalBaseModel):
    """
    Settings for the console mailer
    """

    type: typing.Optional[OtoroshiUtilsMailerConsoleMailerSettingsType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
