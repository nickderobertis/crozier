

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_error_code import MessageErrorCode
from .message_error_content_type import MessageErrorContentType
from .message_info_content_type import MessageInfoContentType


class CheckoutSessionBaseMessagesItem_Info(UniversalBaseModel):
    type: typing.Literal["info"] = "info"
    param: typing.Optional[str] = None
    content_type: MessageInfoContentType
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CheckoutSessionBaseMessagesItem_Error(UniversalBaseModel):
    type: typing.Literal["error"] = "error"
    code: MessageErrorCode
    param: typing.Optional[str] = None
    content_type: MessageErrorContentType
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CheckoutSessionBaseMessagesItem = typing_extensions.Annotated[
    typing.Union[CheckoutSessionBaseMessagesItem_Info, CheckoutSessionBaseMessagesItem_Error],
    pydantic.Field(discriminator="type"),
]
