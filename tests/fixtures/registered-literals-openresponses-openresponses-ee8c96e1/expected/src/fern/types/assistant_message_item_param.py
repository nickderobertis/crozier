

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistant_message_item_param_content import AssistantMessageItemParamContent
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
