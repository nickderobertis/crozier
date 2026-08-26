

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_list_entries_command_type import StorageListEntriesCommandType


class StorageListEntriesCommand(UniversalBaseModel):
    """
    List storage entries at a prefix.

        Navigates storage like a folder tree using delimiter-based listing.
        Returns entries (files/objects) and virtual directories at one level.

        Attributes:
            request_id: Unique identifier for this request.
            namespace: Variable name identifying the storage backend.
            limit: Max entries to return.
            prefix: Path prefix to list (None = root).
            page_token: Token for the next page of entries.
    """

    limit: int
    namespace: str
    page_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageToken"), pydantic.Field(alias="pageToken")
    ] = None
    prefix: typing.Optional[str] = None
    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]
    type: StorageListEntriesCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
