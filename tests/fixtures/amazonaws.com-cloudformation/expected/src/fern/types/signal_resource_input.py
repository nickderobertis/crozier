

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .signal_resource_input_status import SignalResourceInputStatus


class SignalResourceInput(UniversalBaseModel):
    """
    The input for the <a>SignalResource</a> action.
    """

    stack_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackName")] = pydantic.Field()
    """
    The stack name or unique stack ID that includes the resource that you want to signal.
    """

    logical_resource_id: typing_extensions.Annotated[str, FieldMetadata(alias="LogicalResourceId")] = pydantic.Field()
    """
    The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.
    """

    unique_id: typing_extensions.Annotated[str, FieldMetadata(alias="UniqueId")] = pydantic.Field()
    """
    A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.
    """

    status: typing_extensions.Annotated[SignalResourceInputStatus, FieldMetadata(alias="Status")] = pydantic.Field()
    """
    The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
