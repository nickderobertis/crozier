

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .record_handler_progress_input_current_operation_status import RecordHandlerProgressInputCurrentOperationStatus
from .record_handler_progress_input_error_code import RecordHandlerProgressInputErrorCode
from .record_handler_progress_input_operation_status import RecordHandlerProgressInputOperationStatus


class RecordHandlerProgressInput(UniversalBaseModel):
    bearer_token: typing_extensions.Annotated[str, FieldMetadata(alias="BearerToken")] = pydantic.Field()
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    operation_status: typing_extensions.Annotated[
        RecordHandlerProgressInputOperationStatus, FieldMetadata(alias="OperationStatus")
    ] = pydantic.Field()
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    current_operation_status: typing_extensions.Annotated[
        typing.Optional[RecordHandlerProgressInputCurrentOperationStatus], FieldMetadata(alias="CurrentOperationStatus")
    ] = pydantic.Field(default=None)
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    status_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StatusMessage")] = (
        pydantic.Field(default=None)
    )
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    error_code: typing_extensions.Annotated[
        typing.Optional[RecordHandlerProgressInputErrorCode], FieldMetadata(alias="ErrorCode")
    ] = pydantic.Field(default=None)
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    resource_model: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ResourceModel")] = (
        pydantic.Field(default=None)
    )
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    client_request_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ClientRequestToken")
    ] = pydantic.Field(default=None)
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
