

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_utils_mailer_none_mailer_settings_type import OtoroshiUtilsMailerNoneMailerSettingsType


class OtoroshiUtilsMailerNoneMailerSettings(UniversalBaseModel):
    """
    Settings for the /dev/null mailer
    """

    type: typing.Optional[OtoroshiUtilsMailerNoneMailerSettingsType] = pydantic.Field(default=None)
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
