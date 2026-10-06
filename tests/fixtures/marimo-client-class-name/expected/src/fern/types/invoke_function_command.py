

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invoke_function_command_type import InvokeFunctionCommandType
from .request_id import RequestId


class InvokeFunctionCommand(UniversalBaseModel):
    """
    Invoke a function from a UI element.

        Called when a UI element needs to invoke a Python function.

        Attributes:
            function_call_id: Unique identifier for this call.
            namespace: Namespace where the function is registered.
            function_name: Function to invoke.
            args: Keyword arguments for the function.
    """

    args: typing.Dict[str, typing.Any]
    function_call_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="functionCallId"), pydantic.Field(alias="functionCallId")
    ]
    function_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="functionName"), pydantic.Field(alias="functionName")
    ]
    namespace: str
    type: InvokeFunctionCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
