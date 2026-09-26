

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2api_table_row import V2ApiTableRow


class V2BatchInsertRowsData(UniversalBaseModel):
    """
    Rows created by a batch insert.
    """

    rows: typing.List[V2ApiTableRow] = pydantic.Field()
    """
    Inserted table rows.
    """

    inserted_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="insertedCount"),
        pydantic.Field(alias="insertedCount", description="Number of inserted rows."),
    ]
    """
    Number of inserted rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
