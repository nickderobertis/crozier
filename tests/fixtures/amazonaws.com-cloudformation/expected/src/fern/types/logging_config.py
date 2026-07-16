

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LoggingConfig(UniversalBaseModel):
    """
    Contains logging configuration information for an extension.
    """

    log_role_arn: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogRoleArn"),
        pydantic.Field(
            alias="LogRoleArn",
            description="The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.",
        ),
    ]
    """
    The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.
    """

    log_group_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogGroupName"),
        pydantic.Field(
            alias="LogGroupName",
            description="The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.",
        ),
    ]
    """
    The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
