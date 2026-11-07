

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .comment_metadata_model_replied_to import CommentMetadataModelRepliedTo
from .user_model import UserModel


class CommentMetadataModel(UniversalBaseModel):
    message: typing.Optional[str] = None
    marked_up_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="markedUpMessage"), pydantic.Field(alias="markedUpMessage")
    ] = None
    added_participants: typing_extensions.Annotated[
        typing.Optional[typing.List[UserModel]],
        FieldMetadata(alias="addedParticipants"),
        pydantic.Field(alias="addedParticipants"),
    ] = None
    replied_to: typing_extensions.Annotated[
        typing.Optional[CommentMetadataModelRepliedTo],
        FieldMetadata(alias="repliedTo"),
        pydantic.Field(alias="repliedTo"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
