

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .event_action_fs_compress import EventActionFsCompress
from .filesystem_action_types import FilesystemActionTypes
from .key_value import KeyValue
from .rename_config import RenameConfig


class EventActionFilesystemConfig(UniversalBaseModel):
    type: typing.Optional[FilesystemActionTypes] = None
    renames: typing.Optional[typing.List[RenameConfig]] = None
    mkdirs: typing.Optional[typing.List[str]] = None
    deletes: typing.Optional[typing.List[str]] = None
    exist: typing.Optional[typing.List[str]] = None
    copy_: typing_extensions.Annotated[
        typing.Optional[typing.List[KeyValue]], FieldMetadata(alias="copy"), pydantic.Field(alias="copy")
    ] = None
    compress: typing.Optional[EventActionFsCompress] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
