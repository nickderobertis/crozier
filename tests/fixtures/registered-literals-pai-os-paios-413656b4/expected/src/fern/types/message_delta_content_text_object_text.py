

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_text_object_text_annotations_item import MessageDeltaContentTextObjectTextAnnotationsItem


class MessageDeltaContentTextObjectText(UniversalBaseModel):
    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The data that makes up the text.
    """

    annotations: typing.Optional[typing.List[MessageDeltaContentTextObjectTextAnnotationsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
