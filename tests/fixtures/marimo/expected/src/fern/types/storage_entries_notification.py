

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .storage_entries_notification_op import StorageEntriesNotificationOp
from .storage_entry import StorageEntry


class StorageEntriesNotification(UniversalBaseModel):
    """
    Result of a storage operation that returns entries.

        Attributes:
            request_id: Request ID this responds to.
            entries: Storage entries returned by the operation.
            namespace: Variable name of the storage backend.
            prefix: The prefix that was listed (set by list_entries).
            query: The search query that was used (set by search).
            next_page_token: Token for fetching the next page of entries.
            error: Error message if the operation failed.
    """

    entries: typing.List[StorageEntry]
    error: typing.Optional[str] = None
    namespace: str
    next_page_token: typing.Optional[str] = None
    op: StorageEntriesNotificationOp
    prefix: typing.Optional[str] = None
    query: typing.Optional[str] = None
    request_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
