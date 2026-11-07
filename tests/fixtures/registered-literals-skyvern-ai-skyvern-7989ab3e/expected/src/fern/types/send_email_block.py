

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .aws_secret_parameter import AwsSecretParameter
from .email_body_format import EmailBodyFormat
from .output_parameter import OutputParameter


class SendEmailBlock(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Author-facing identifier for a block; unique within a workflow.
    """

    next_block_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional pointer to the next block label when constructing a DAG. Defaults to sequential order when omitted.
    """

    output_parameter: OutputParameter
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    disable_cache: typing.Optional[bool] = None
    ignore_workflow_system_prompt: typing.Optional[bool] = None
    next_loop_on_failure: typing.Optional[bool] = None
    smtp_host: AwsSecretParameter
    smtp_port: AwsSecretParameter
    smtp_username: AwsSecretParameter
    smtp_password: AwsSecretParameter
    sender: str
    recipients: typing.List[str]
    subject: str
    body: str
    body_format: typing.Optional[EmailBodyFormat] = None
    file_attachments: typing.Optional[typing.List[str]] = None
    custom_smtp_host: typing.Optional[str] = None
    custom_smtp_port: typing.Optional[int] = None
    custom_smtp_username: typing.Optional[str] = None
    custom_smtp_password: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
