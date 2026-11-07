

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sqlite_execute_request_statement_args_args import SqliteExecuteRequestStatementArgsArgs


class SqliteExecuteRequestStatementArgs(UniversalBaseModel):
    """
    A parameterized SQL query. See https://docs.turso.tech/sdk/ts/reference#batch-transactions for reference
    """

    sql: str = pydantic.Field()
    """
    SQL statement, with ? placeholders for arguments
    """

    args: SqliteExecuteRequestStatementArgsArgs = pydantic.Field()
    """
    List of arguments to be used in the given statement
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
