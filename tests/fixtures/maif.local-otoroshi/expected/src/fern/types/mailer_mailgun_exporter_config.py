

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mailer_mailgun_exporter_config_type import MailerMailgunExporterConfigType


class MailerMailgunExporterConfig(UniversalBaseModel):
    api_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKey"),
        pydantic.Field(alias="apiKey", description="Mailgun apiKey"),
    ] = None
    """
    Mailgun apiKey
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mailgun domain
    """

    eu: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the mailgun server is european
    """

    to: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Email adresses of recipents
    """

    type: MailerMailgunExporterConfigType = pydantic.Field()
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
