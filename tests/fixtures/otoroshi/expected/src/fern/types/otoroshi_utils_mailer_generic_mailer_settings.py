

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_utils_mailer_email_location import OtoroshiUtilsMailerEmailLocation
from .otoroshi_utils_mailer_generic_mailer_settings_type import OtoroshiUtilsMailerGenericMailerSettingsType


class OtoroshiUtilsMailerGenericMailerSettings(UniversalBaseModel):
    """
    Settings for the generic mailer (http requests)
    """

    type: typing.Optional[OtoroshiUtilsMailerGenericMailerSettingsType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sender URL
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Sender headers
    """

    to: typing.Optional[typing.List[OtoroshiUtilsMailerEmailLocation]] = pydantic.Field(default=None)
    """
    Destination email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
