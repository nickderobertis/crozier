

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_json_schema import StreamJsonSchema
from .sync_mode import SyncMode


class AirbyteStream(UniversalBaseModel):
    """
    the immutable schema defined by the source
    """

    default_cursor_field: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="defaultCursorField")
    ] = pydantic.Field(default=None)
    """
    Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves.
    """

    json_schema: typing_extensions.Annotated[typing.Optional[StreamJsonSchema], FieldMetadata(alias="jsonSchema")] = (
        None
    )
    name: str = pydantic.Field()
    """
    Stream's name.
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional Source-defined namespace. Airbyte streams from the same sources should have the same namespace. Currently only used by JDBC destinations to determine what schema to write to.
    """

    source_defined_cursor: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="sourceDefinedCursor")
    ] = pydantic.Field(default=None)
    """
    If the source defines the cursor field, then any other cursor field inputs will be ignored. If it does not, either the user_provided one is used, or the default one is used as a backup.
    """

    source_defined_primary_key: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[str]]], FieldMetadata(alias="sourceDefinedPrimaryKey")
    ] = pydantic.Field(default=None)
    """
    If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves.
    """

    supported_sync_modes: typing_extensions.Annotated[
        typing.Optional[typing.List[SyncMode]], FieldMetadata(alias="supportedSyncModes")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
