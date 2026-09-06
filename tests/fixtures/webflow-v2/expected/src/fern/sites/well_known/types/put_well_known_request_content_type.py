

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class PutWellKnownRequestContentType(enum.StrEnum):
    """
    The content type of the file. Defaults to application/json
    """

    APPLICATION_JSON = "application/json"
    TEXT_PLAIN = "text/plain"

    def visit(
        self, application_json: typing.Callable[[], T_Result], text_plain: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PutWellKnownRequestContentType.APPLICATION_JSON:
            return application_json()
        if self is PutWellKnownRequestContentType.TEXT_PLAIN:
            return text_plain()
