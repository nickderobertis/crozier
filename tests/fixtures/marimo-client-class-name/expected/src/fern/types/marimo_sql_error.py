

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_sql_error_type import MarimoSqlErrorType


class MarimoSqlError(UniversalBaseModel):
    """
    SQL-specific error with enhanced metadata for debugging.
    """

    hint: typing.Optional[str] = None
    msg: str
    node_col_offset: typing.Optional[int] = None
    node_lineno: typing.Optional[int] = None
    sql_col: typing.Optional[int] = None
    sql_line: typing.Optional[int] = None
    sql_statement: str
    type: MarimoSqlErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
