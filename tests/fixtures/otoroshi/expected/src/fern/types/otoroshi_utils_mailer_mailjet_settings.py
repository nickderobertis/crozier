

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_utils_mailer_email_location import OtoroshiUtilsMailerEmailLocation
from .otoroshi_utils_mailer_mailjet_settings_type import OtoroshiUtilsMailerMailjetSettingsType


class OtoroshiUtilsMailerMailjetSettings(UniversalBaseModel):
    """
    Settings for the mailjet mailer
    """

    type: typing.Optional[OtoroshiUtilsMailerMailjetSettingsType] = pydantic.Field(default=None)
    """
    the kind of exporter
    """

    api_key_public: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKeyPublic"),
        pydantic.Field(alias="apiKeyPublic", description="Public key"),
    ] = None
    """
    Public key
    """

    api_key_private: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKeyPrivate"),
        pydantic.Field(alias="apiKeyPrivate", description="Private key"),
    ] = None
    """
    Private key
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
