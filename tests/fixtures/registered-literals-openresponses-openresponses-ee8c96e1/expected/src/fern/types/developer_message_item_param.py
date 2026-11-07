

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .developer_message_item_param_content import DeveloperMessageItemParamContent
from .developer_message_item_param_role import DeveloperMessageItemParamRole
from .developer_message_item_param_type import DeveloperMessageItemParamType


class DeveloperMessageItemParam(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of this message item.
    """

    type: DeveloperMessageItemParamType = pydantic.Field()
    """
    The item type. Always `message`.
    """

    role: DeveloperMessageItemParamRole = pydantic.Field()
    """
    The message role. Always `developer`.
    """

    content: DeveloperMessageItemParamContent = pydantic.Field()
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
