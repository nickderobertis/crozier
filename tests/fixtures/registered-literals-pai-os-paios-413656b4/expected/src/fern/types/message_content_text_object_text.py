

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_text_object_text_annotations_item import MessageContentTextObjectTextAnnotationsItem


class MessageContentTextObjectText(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    The data that makes up the text.
    """

    annotations: typing.List[MessageContentTextObjectTextAnnotationsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
