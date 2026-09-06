

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .setting_multi_source_integer import SettingMultiSourceInteger
from .setting_multi_source_string import SettingMultiSourceString
from .settings_dto_thumbnail_size import SettingsDtoThumbnailSize


class SettingsDto(UniversalBaseModel):
    delete_empty_collections: typing_extensions.Annotated[
        bool, FieldMetadata(alias="deleteEmptyCollections"), pydantic.Field(alias="deleteEmptyCollections")
    ]
    delete_empty_read_lists: typing_extensions.Annotated[
        bool, FieldMetadata(alias="deleteEmptyReadLists"), pydantic.Field(alias="deleteEmptyReadLists")
    ]
    kepubify_path: typing_extensions.Annotated[
        SettingMultiSourceString, FieldMetadata(alias="kepubifyPath"), pydantic.Field(alias="kepubifyPath")
    ]
    kobo_port: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="koboPort"), pydantic.Field(alias="koboPort")
    ] = None
    kobo_proxy: typing_extensions.Annotated[bool, FieldMetadata(alias="koboProxy"), pydantic.Field(alias="koboProxy")]
    remember_me_duration_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="rememberMeDurationDays"), pydantic.Field(alias="rememberMeDurationDays")
    ]
    server_context_path: typing_extensions.Annotated[
        SettingMultiSourceString, FieldMetadata(alias="serverContextPath"), pydantic.Field(alias="serverContextPath")
    ]
    server_port: typing_extensions.Annotated[
        SettingMultiSourceInteger, FieldMetadata(alias="serverPort"), pydantic.Field(alias="serverPort")
    ]
    task_pool_size: typing_extensions.Annotated[
        int, FieldMetadata(alias="taskPoolSize"), pydantic.Field(alias="taskPoolSize")
    ]
    thumbnail_size: typing_extensions.Annotated[
        SettingsDtoThumbnailSize, FieldMetadata(alias="thumbnailSize"), pydantic.Field(alias="thumbnailSize")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
