

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseUnreadMsgsHuddlesItem(UniversalBaseModel):
    user_ids_string: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string containing the IDs of all users in the group
    direct message conversation, including the current user,
    separated by commas and sorted numerically; for example:
    `"1,2,3"`.
    """

    unread_message_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The message IDs of the recent unread messages which have been sent in
    this group direct message conversation, sorted in ascending order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
