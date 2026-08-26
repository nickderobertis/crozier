

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sql_parse_error_severity import SqlParseErrorSeverity


class SqlParseError(UniversalBaseModel):
    """
    Represents a single SQL parse error.

    Attributes:
        message (str): Description of the error.
        line (int): Line number where the error occurred (1-based).
        column (int): Column number where the error occurred (1-based).
        severity (Literal["error", "warning"]): Severity of the error.
    """

    column: int
    line: int
    message: str
    severity: SqlParseErrorSeverity

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
