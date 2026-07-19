

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .letta_schemas_message_tool_return_output_func_response import LettaSchemasMessageToolReturnOutputFuncResponse
from .letta_schemas_message_tool_return_output_status import LettaSchemasMessageToolReturnOutputStatus


class LettaSchemasMessageToolReturnOutput(UniversalBaseModel):
    tool_call_id: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The ID for the tool call
    """

    status: LettaSchemasMessageToolReturnOutputStatus = pydantic.Field()
    """
    The status of the tool call
    """

    stdout: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Captured stdout (e.g. prints, logs) from the tool invocation
    """

    stderr: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Captured stderr from the tool invocation
    """

    func_response: typing.Optional[LettaSchemasMessageToolReturnOutputFuncResponse] = pydantic.Field(default=None)
    """
    The function response - either a string or list of content parts (text/image)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
