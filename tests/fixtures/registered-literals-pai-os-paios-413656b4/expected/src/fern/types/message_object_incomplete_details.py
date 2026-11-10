

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_object_incomplete_details_reason import MessageObjectIncompleteDetailsReason


class MessageObjectIncompleteDetails(UniversalBaseModel):
    """
    On an incomplete message, details about why the message is incomplete.
    """

    reason: MessageObjectIncompleteDetailsReason = pydantic.Field()
    """
    The reason the message is incomplete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
