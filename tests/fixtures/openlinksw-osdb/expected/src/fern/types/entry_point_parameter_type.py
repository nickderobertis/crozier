

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryPointParameterType(enum.StrEnum):
    """
    The type of the parameter, indicating its location in the HTTP request.
    """

    QUERY = "query"
    HEADER = "header"
    URI = "uri"
    PATH = "path"
    BODY = "body"

    def visit(
        self,
        query: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
        uri: typing.Callable[[], T_Result],
        path: typing.Callable[[], T_Result],
        body: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryPointParameterType.QUERY:
            return query()
        if self is EntryPointParameterType.HEADER:
            return header()
        if self is EntryPointParameterType.URI:
            return uri()
        if self is EntryPointParameterType.PATH:
            return path()
        if self is EntryPointParameterType.BODY:
            return body()
