

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .action_attachment import ActionAttachment


class ActUpdateRequestAttachments(UniversalBaseModel):
    message: typing.Optional[str] = None
    attachments: typing.Optional[typing.List[ActionAttachment]] = None
    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
