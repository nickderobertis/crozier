

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mailer_mailjet_exporter_config_type import MailerMailjetExporterConfigType


class MailerMailjetExporterConfig(UniversalBaseModel):
    api_key_private: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiKeyPrivate")] = (
        pydantic.Field(default=None)
    )
    """
    Mailjet private apiKey
    """

    api_key_public: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiKeyPublic")] = (
        pydantic.Field(default=None)
    )
    """
    Mailjet public apiKey
    """

    to: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Email adresses of recipents
    """

    type: MailerMailjetExporterConfigType = pydantic.Field()
    """
    Type of mailer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
