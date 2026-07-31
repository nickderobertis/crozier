

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionError(enum.StrEnum):
    """
    Structured failure mode. `conflict` corresponds to an
    `expectedRevision` mismatch on a note update. Today most
    host-side crashes surface as `unknown` (raw nack); future
    work will route revision-mismatch and visibility errors to
    their typed variants.
    """

    NOT_AUTHORIZED = "not-authorized"
    NOT_FOUND = "not-found"
    INVALID_NAME = "invalid-name"
    CONFLICT = "conflict"
    REQUEST_TOO_LARGE = "request-too-large"
    UNKNOWN = "unknown"

    def visit(
        self,
        not_authorized: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        invalid_name: typing.Callable[[], T_Result],
        conflict: typing.Callable[[], T_Result],
        request_too_large: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionError.NOT_AUTHORIZED:
            return not_authorized()
        if self is ActionError.NOT_FOUND:
            return not_found()
        if self is ActionError.INVALID_NAME:
            return invalid_name()
        if self is ActionError.CONFLICT:
            return conflict()
        if self is ActionError.REQUEST_TOO_LARGE:
            return request_too_large()
        if self is ActionError.UNKNOWN:
            return unknown()
