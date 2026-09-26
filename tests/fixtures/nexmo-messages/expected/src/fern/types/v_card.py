

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .v_card_message_type import VCardMessageType
from .v_card_vcard import VCardVcard


class VCard(BaseMessageType):
    message_type: typing.Optional[VCardMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `vcard` in this field
    """

    vcard: VCardVcard

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
