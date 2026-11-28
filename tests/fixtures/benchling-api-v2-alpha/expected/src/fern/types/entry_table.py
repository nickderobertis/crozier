

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_table_row import EntryTableRow


class EntryTable(UniversalBaseModel):
    """
    Actual tabular data with rows and columns of text on the note.
    """

    column_labels: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Optional[str]]],
        FieldMetadata(alias="columnLabels"),
        pydantic.Field(
            alias="columnLabels",
            description="Array of strings, with one item per column. Defaults to null, if the user is using the default, but is set if the user has given a custom name to the column.",
        ),
    ] = None
    """
    Array of strings, with one item per column. Defaults to null, if the user is using the default, but is set if the user has given a custom name to the column.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the table - defaults to e.g. Table1 but can be renamed.
    """

    rows: typing.Optional[typing.List[EntryTableRow]] = pydantic.Field(default=None)
    """
    Array of row objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
