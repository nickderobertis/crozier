

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DraftReplyResponse(UniversalBaseModel):
    draft_reply: typing_extensions.Annotated[str, FieldMetadata(alias="draftReply"), pydantic.Field(alias="draftReply")]
    provider: typing.Optional[str] = None
    model: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
