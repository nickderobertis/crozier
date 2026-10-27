

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_files_folder_file_system_info import ChannelFilesFolderFileSystemInfo
from .channel_files_folder_folder import ChannelFilesFolderFolder
from .channel_files_folder_parent_reference import ChannelFilesFolderParentReference


class ChannelFilesFolder(UniversalBaseModel):
    id: typing.Optional[str] = None
    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    last_modified_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModifiedDateTime"),
        pydantic.Field(alias="lastModifiedDateTime"),
    ] = None
    name: typing.Optional[str] = None
    web_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webUrl"), pydantic.Field(alias="webUrl")
    ] = None
    size: typing.Optional[int] = None
    parent_reference: typing_extensions.Annotated[
        typing.Optional[ChannelFilesFolderParentReference],
        FieldMetadata(alias="parentReference"),
        pydantic.Field(alias="parentReference"),
    ] = None
    file_system_info: typing_extensions.Annotated[
        typing.Optional[ChannelFilesFolderFileSystemInfo],
        FieldMetadata(alias="fileSystemInfo"),
        pydantic.Field(alias="fileSystemInfo"),
    ] = None
    folder: typing.Optional[ChannelFilesFolderFolder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
