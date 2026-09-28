

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2move_tables_data_skipped_item_kind import V2MoveTablesDataSkippedItemKind


class V2MoveTablesDataSkippedItem(UniversalBaseModel):
    kind: V2MoveTablesDataSkippedItemKind = pydantic.Field()
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
