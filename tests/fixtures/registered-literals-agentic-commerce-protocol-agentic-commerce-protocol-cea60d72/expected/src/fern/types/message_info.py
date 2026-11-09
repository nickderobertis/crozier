

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_info_content_type import MessageInfoContentType


class MessageInfo(UniversalBaseModel):
    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    RFC 9535 JSONPath
    """

    content_type: MessageInfoContentType
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
