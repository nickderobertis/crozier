

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendEmailBlockYaml(UniversalBaseModel):
    label: str
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    smtp_host_secret_parameter_key: str
    smtp_port_secret_parameter_key: str
    smtp_username_secret_parameter_key: str
    smtp_password_secret_parameter_key: str
    sender: str
    recipients: typing.List[str]
    subject: str
    body: str
    file_attachments: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
