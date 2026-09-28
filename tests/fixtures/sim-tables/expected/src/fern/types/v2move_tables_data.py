

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2move_tables_data_failed_item import V2MoveTablesDataFailedItem
from .v2move_tables_data_moved_item import V2MoveTablesDataMovedItem
from .v2move_tables_data_not_found_item import V2MoveTablesDataNotFoundItem
from .v2move_tables_data_skipped_item import V2MoveTablesDataSkippedItem


class V2MoveTablesData(UniversalBaseModel):
    """
    Per-item outcome of a bulk table and folder move.
    """

    moved: typing.List[V2MoveTablesDataMovedItem] = pydantic.Field()
    """
    Items the batch moved.
    """

    skipped: typing.List[V2MoveTablesDataSkippedItem] = pydantic.Field()
    """
    Items dropped because a selected folder already carries them.
    """

    not_found: typing_extensions.Annotated[
        typing.List[V2MoveTablesDataNotFoundItem],
        FieldMetadata(alias="notFound"),
        pydantic.Field(alias="notFound", description="Entries nothing active resolved to."),
    ]
    """
    Entries nothing active resolved to.
    """

    failed: typing.List[V2MoveTablesDataFailedItem] = pydantic.Field()
    """
    Items the batch could not move.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
