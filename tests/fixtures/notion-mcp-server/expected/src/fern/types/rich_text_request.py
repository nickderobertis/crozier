

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rich_text_request_text import RichTextRequestText
from .rich_text_request_type import RichTextRequestType


class RichTextRequest(UniversalBaseModel):
    text: RichTextRequestText
    type: typing.Optional[RichTextRequestType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
