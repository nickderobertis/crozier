

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MailerSettings(UniversalBaseModel):
    """
    Configuration for mailgun api client
    """

    api_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey", description="Mailgun mailer api key")
    ]
    """
    Mailgun mailer api key
    """

    api_key_private: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKeyPrivate"),
        pydantic.Field(alias="apiKeyPrivate", description="Mailjet mailer private api key"),
    ] = None
    """
    Mailjet mailer private api key
    """

    api_key_public: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKeyPublic"),
        pydantic.Field(alias="apiKeyPublic", description="Mailjet mailer public api key"),
    ] = None
    """
    Mailjet mailer public api key
    """

    domain: str = pydantic.Field()
    """
    Mailgun mailer domain
    """

    eu: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Mailgun mailer, use EU tenant api
    """

    header: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Generic mailer headers
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the mailer: console, generic, mailgun, mailjet
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Generic mailer url
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
