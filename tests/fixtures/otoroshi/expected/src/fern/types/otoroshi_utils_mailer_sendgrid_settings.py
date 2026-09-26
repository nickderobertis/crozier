

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_utils_mailer_email_location import OtoroshiUtilsMailerEmailLocation
from .otoroshi_utils_mailer_sendgrid_settings_type import OtoroshiUtilsMailerSendgridSettingsType


class OtoroshiUtilsMailerSendgridSettings(UniversalBaseModel):
    """
    Settings for the sendgrid mailer
    """

    type: typing.Optional[OtoroshiUtilsMailerSendgridSettingsType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    api_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKey"),
        pydantic.Field(alias="apiKey", description="Sendgrid apikey"),
    ] = None
    """
    Sendgrid apikey
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
