

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_files_paginated_list_connection_files_item_data_type import (
    ConnectionFilesPaginatedListConnectionFilesItemDataType,
)
from .connection_files_paginated_list_connection_files_item_status import (
    ConnectionFilesPaginatedListConnectionFilesItemStatus,
)


class ConnectionFilesPaginatedListConnectionFilesItem(UniversalBaseModel):
    connection_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    data_type: typing_extensions.Annotated[
        typing.Optional[ConnectionFilesPaginatedListConnectionFilesItemDataType],
        FieldMetadata(alias="dataType"),
        pydantic.Field(alias="dataType"),
    ] = None
    download_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="downloadUrl"),
        pydantic.Field(
            alias="downloadUrl", description="URL to download the file. This URL is only valid for 24 hours."
        ),
    ] = None
    """
    URL to download the file. This URL is only valid for 24 hours.
    """

    filename: typing.Optional[str] = None
    id: typing.Optional[str] = None
    instrument_query_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="instrumentQueryId"), pydantic.Field(alias="instrumentQueryId")
    ] = None
    modified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ] = None
    status: typing.Optional[ConnectionFilesPaginatedListConnectionFilesItemStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
