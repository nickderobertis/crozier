

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_utils_mailer_email_location import OtoroshiUtilsMailerEmailLocation
from .otoroshi_utils_mailer_mailgun_settings_type import OtoroshiUtilsMailerMailgunSettingsType


class OtoroshiUtilsMailerMailgunSettings(UniversalBaseModel):
    """
    Settings for the mailgun mailer
    """

    type: typing.Optional[OtoroshiUtilsMailerMailgunSettingsType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    eu: typing.Optional[bool] = pydantic.Field(default=None)
    """
    European tenant
    """

    api_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKey"),
        pydantic.Field(alias="apiKey", description="Mailgun apikey"),
    ] = None
    """
    Mailgun apikey
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mailgun domain
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
