

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mailer_console_exporter_config_type import MailerConsoleExporterConfigType


class MailerConsoleExporterConfig(UniversalBaseModel):
    type: typing.Optional[MailerConsoleExporterConfigType] = pydantic.Field(default=None)
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
