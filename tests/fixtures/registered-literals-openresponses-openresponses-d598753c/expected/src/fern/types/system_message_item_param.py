

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .system_message_item_param_content import SystemMessageItemParamContent
from .system_message_item_param_role import SystemMessageItemParamRole
from .system_message_item_param_type import SystemMessageItemParamType


class SystemMessageItemParam(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of this message item.
    """

    type: SystemMessageItemParamType = pydantic.Field()
    """
    The item type. Always `message`.
    """

    role: SystemMessageItemParamRole = pydantic.Field()
    """
    The message role. Always `system`.
    """

    content: SystemMessageItemParamContent = pydantic.Field()
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
