

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_sync_mode import DestinationSyncMode
from .selected_field_info import SelectedFieldInfo
from .sync_mode import SyncMode


class AirbyteStreamConfiguration(UniversalBaseModel):
    """
    the mutable part of the stream to configure the destination
    """

    alias_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="aliasName")] = pydantic.Field(
        default=None
    )
    """
    Alias name to the stream to be used in the destination
    """

    cursor_field: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="cursorField")] = (
        pydantic.Field(default=None)
    )
    """
    Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored.
    """

    destination_sync_mode: typing_extensions.Annotated[DestinationSyncMode, FieldMetadata(alias="destinationSyncMode")]
    field_selection_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fieldSelectionEnabled")
    ] = pydantic.Field(default=None)
    """
    Whether field selection should be enabled. If this is true, only the properties in `selectedFields` will be included.
    """

    primary_key: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[str]]], FieldMetadata(alias="primaryKey")
    ] = pydantic.Field(default=None)
    """
    Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup`. Otherwise it is ignored.
    """

    selected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, the stream is selected with all of its properties. For new connections, this considers if the stream is suggested or not
    """

    selected_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[SelectedFieldInfo]], FieldMetadata(alias="selectedFields")
    ] = pydantic.Field(default=None)
    """
    Paths to the fields that will be included in the configured catalog. This must be set if `fieldSelectedEnabled` is set. An empty list indicates that no properties will be included.
    """

    suggested: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Does the connector suggest that this stream be enabled by default?
    """

    sync_mode: typing_extensions.Annotated[SyncMode, FieldMetadata(alias="syncMode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
