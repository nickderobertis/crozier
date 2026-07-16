

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mailer_generic_exporter_config_type import MailerGenericExporterConfigType


class MailerGenericExporterConfig(UniversalBaseModel):
    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Optional headers
    """

    to: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Email adresses of recipents
    """

    type: MailerGenericExporterConfigType = pydantic.Field()
    """
    Type of mailer
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Url of mailer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
