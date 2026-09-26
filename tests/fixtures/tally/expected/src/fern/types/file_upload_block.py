

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_uuid import BlockUuid
from .file_upload_block_group_type import FileUploadBlockGroupType
from .file_upload_payload import FileUploadPayload
from .group_uuid import GroupUuid


class FileUploadBlock(UniversalBaseModel):
    """
    A block with type FILE_UPLOAD. Used for file upload input.
    """

    uuid_: typing_extensions.Annotated[BlockUuid, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    group_uuid: typing_extensions.Annotated[
        GroupUuid, FieldMetadata(alias="groupUuid"), pydantic.Field(alias="groupUuid")
    ]
    group_type: typing_extensions.Annotated[
        FileUploadBlockGroupType, FieldMetadata(alias="groupType"), pydantic.Field(alias="groupType")
    ]
    payload: FileUploadPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
