

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_tool_schema import ClientToolSchema
from .letta_batch_request_input import LettaBatchRequestInput
from .letta_batch_request_messages_item import LettaBatchRequestMessagesItem
from .message_type import MessageType


class LettaBatchRequest(UniversalBaseModel):
    messages: typing.Optional[typing.List[LettaBatchRequestMessagesItem]] = pydantic.Field(default=None)
    """
    The messages to be sent to the agent.
    """

    input: typing.Optional[LettaBatchRequestInput] = pydantic.Field(default=None)
    """
    Syntactic sugar for a single user message. Equivalent to messages=[{'role': 'user', 'content': input}].
    """

    max_steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of steps the agent should take to process the request.
    """

    use_assistant_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.
    """

    assistant_message_tool_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.
    """

    assistant_message_tool_kwarg: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the message argument in the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.
    """

    include_return_message_types: typing.Optional[typing.List[MessageType]] = pydantic.Field(default=None)
    """
    Only return specified message types in the response. If `None` (default) returns all messages.
    """

    enable_thinking: typing.Optional[str] = pydantic.Field(default=None)
    """
    If set to True, enables reasoning before responses or tool calls from the agent.
    """

    client_tools: typing.Optional[typing.List[ClientToolSchema]] = pydantic.Field(default=None)
    """
    Client-side tools that the agent can call. When the agent calls a client-side tool, execution pauses and returns control to the client to execute the tool and provide the result via a ToolReturn.
    """

    override_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model handle to use for this request instead of the agent's default model. This allows sending a message to a different model without changing the agent's configuration.
    """

    agent_id: str = pydantic.Field()
    """
    The ID of the agent to send this batch request for
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
