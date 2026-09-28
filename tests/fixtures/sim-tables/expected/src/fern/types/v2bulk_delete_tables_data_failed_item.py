

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2bulk_delete_tables_data_failed_item_kind import V2BulkDeleteTablesDataFailedItemKind


class V2BulkDeleteTablesDataFailedItem(UniversalBaseModel):
    kind: V2BulkDeleteTablesDataFailedItemKind = pydantic.Field()
    """
    Which kind of item this entry names.
    """

    id: str = pydantic.Field()
    """
    Table identifier, or the folder path for a folder.
    """

    name: str = pydantic.Field()
    """
    Table name, or the folder path for a folder.
    """

    reason: str = pydantic.Field()
    """
    Why this item could not be acted on.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
