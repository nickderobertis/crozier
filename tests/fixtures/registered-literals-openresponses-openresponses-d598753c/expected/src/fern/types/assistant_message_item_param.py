

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistant_message_item_param_content import AssistantMessageItemParamContent
from .assistant_message_item_param_phase import AssistantMessageItemParamPhase
from .assistant_message_item_param_role import AssistantMessageItemParamRole
from .assistant_message_item_param_type import AssistantMessageItemParamType


class AssistantMessageItemParam(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of this message item.
    """

    type: AssistantMessageItemParamType = pydantic.Field()
    """
    The item type. Always `message`.
    """

    role: AssistantMessageItemParamRole = pydantic.Field()
    """
    The role of the message author. Always `assistant`.
    """

    content: AssistantMessageItemParamContent = pydantic.Field()
    """
    The message content, as an array of content parts.
    """

    phase: typing.Optional[AssistantMessageItemParamPhase] = pydantic.Field(default=None)
    """
    Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages. Omitting it can degrade performance. Not used for user messages.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the message item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
