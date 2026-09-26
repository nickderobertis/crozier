

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_uuid import BlockUuid
from .embed_video_block_group_type import EmbedVideoBlockGroupType
from .embed_video_payload import EmbedVideoPayload
from .group_uuid import GroupUuid


class EmbedVideoBlock(UniversalBaseModel):
    """
    A block with type EMBED_VIDEO. Used for embedding video content.
    """

    uuid_: typing_extensions.Annotated[BlockUuid, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    group_uuid: typing_extensions.Annotated[
        GroupUuid, FieldMetadata(alias="groupUuid"), pydantic.Field(alias="groupUuid")
    ]
    group_type: typing_extensions.Annotated[
        EmbedVideoBlockGroupType, FieldMetadata(alias="groupType"), pydantic.Field(alias="groupType")
    ]
    payload: EmbedVideoPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
