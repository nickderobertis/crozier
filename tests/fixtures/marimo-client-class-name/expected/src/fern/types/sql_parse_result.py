

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sql_parse_error import SqlParseError


class SqlParseResult(UniversalBaseModel):
    """
    Result of parsing an SQL query.

    Attributes:
        success (bool): True if parsing succeeded without errors.
        errors (list[SqlParseError]): List of parse errors (empty if success is True).
    """

    errors: typing.List[SqlParseError]
    success: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
