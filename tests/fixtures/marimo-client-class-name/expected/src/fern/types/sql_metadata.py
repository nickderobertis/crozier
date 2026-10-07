

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sql_metadata_type import SqlMetadataType


class SqlMetadata(UniversalBaseModel):
    """
    SQL database and schema metadata.

        Attributes:
            connection: Connection identifier.
            database: Database name.
            schema: Schema name.
            schema_path: Path of nested schemas (relative to `database`). Empty
                for the top level.
    """

    connection: str
    database: str
    schema_: typing_extensions.Annotated[str, FieldMetadata(alias="schema"), pydantic.Field(alias="schema")]
    schema_path: typing.Optional[typing.List[str]] = None
    type: SqlMetadataType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
