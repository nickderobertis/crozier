

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_content_get import MessageContentGet
from .template_ref_get import TemplateRefGet


class TemplatePreviewGet(UniversalBaseModel):
    ref: TemplateRefGet
    message_content: typing_extensions.Annotated[
        MessageContentGet, FieldMetadata(alias="messageContent"), pydantic.Field(alias="messageContent")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
