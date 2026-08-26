

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .request_id import RequestId
from .validate_sql_command_type import ValidateSqlCommandType


class ValidateSqlCommand(UniversalBaseModel):
    """
    Validate an SQL query.

        Checks if an SQL query is valid by parsing against a dialect (no DB connection)
        or validating against an actual database.

        Attributes:
            request_id: Unique identifier for this request.
            query: SQL query to validate.
            only_parse: If True, only parse using dialect. If False, validate against DB.
            engine: SQL engine (required if only_parse is False).
            dialect: SQL dialect for parsing (required if only_parse is True).
    """

    dialect: typing.Optional[str] = None
    engine: typing.Optional[str] = None
    only_parse: typing_extensions.Annotated[bool, FieldMetadata(alias="onlyParse"), pydantic.Field(alias="onlyParse")]
    query: str
    request_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ]
    type: ValidateSqlCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
