

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2bulk_delete_tables_data_deleted_item import V2BulkDeleteTablesDataDeletedItem
from .v2bulk_delete_tables_data_deleted_items import V2BulkDeleteTablesDataDeletedItems
from .v2bulk_delete_tables_data_failed_item import V2BulkDeleteTablesDataFailedItem
from .v2bulk_delete_tables_data_not_found_item import V2BulkDeleteTablesDataNotFoundItem
from .v2bulk_delete_tables_data_skipped_item import V2BulkDeleteTablesDataSkippedItem


class V2BulkDeleteTablesData(UniversalBaseModel):
    """
    Per-item outcome of a bulk table and folder delete.
    """

    deleted: typing.List[V2BulkDeleteTablesDataDeletedItem] = pydantic.Field()
    """
    Items the batch archived or deleted.
    """

    skipped: typing.List[V2BulkDeleteTablesDataSkippedItem] = pydantic.Field()
    """
    Items dropped because a selected folder already carries them.
    """

    not_found: typing_extensions.Annotated[
        typing.List[V2BulkDeleteTablesDataNotFoundItem],
        FieldMetadata(alias="notFound"),
        pydantic.Field(alias="notFound", description="Entries nothing active resolved to."),
    ]
    """
    Entries nothing active resolved to.
    """

    failed: typing.List[V2BulkDeleteTablesDataFailedItem] = pydantic.Field()
    """
    Items the batch could not delete.
    """

    deleted_items: typing_extensions.Annotated[
        V2BulkDeleteTablesDataDeletedItems,
        FieldMetadata(alias="deletedItems"),
        pydantic.Field(
            alias="deletedItems",
            description="Totals across the explicit archives and every folder cascade they triggered.",
        ),
    ]
    """
    Totals across the explicit archives and every folder cascade they triggered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
