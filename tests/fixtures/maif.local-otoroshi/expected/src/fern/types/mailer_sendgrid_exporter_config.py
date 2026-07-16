

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mailer_sendgrid_exporter_config_type import MailerSendgridExporterConfigType


class MailerSendgridExporterConfig(UniversalBaseModel):
    api_key_public: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiKeyPublic")] = (
        pydantic.Field(default=None)
    )
    """
    Sendgrid apiKey
    """

    to: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Email adresses of recipents
    """

    type: MailerSendgridExporterConfigType = pydantic.Field()
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
