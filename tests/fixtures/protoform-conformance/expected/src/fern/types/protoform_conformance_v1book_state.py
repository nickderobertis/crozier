

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProtoformConformanceV1BookState(enum.StrEnum):
    BOOK_STATE_UNSPECIFIED = "BOOK_STATE_UNSPECIFIED"
    BOOK_STATE_ACTIVE = "BOOK_STATE_ACTIVE"
    BOOK_STATE_DELETING = "BOOK_STATE_DELETING"
    BOOK_STATE_DELETED = "BOOK_STATE_DELETED"

    def visit(
        self,
        book_state_unspecified: typing.Callable[[], T_Result],
        book_state_active: typing.Callable[[], T_Result],
        book_state_deleting: typing.Callable[[], T_Result],
        book_state_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProtoformConformanceV1BookState.BOOK_STATE_UNSPECIFIED:
            return book_state_unspecified()
        if self is ProtoformConformanceV1BookState.BOOK_STATE_ACTIVE:
            return book_state_active()
        if self is ProtoformConformanceV1BookState.BOOK_STATE_DELETING:
            return book_state_deleting()
        if self is ProtoformConformanceV1BookState.BOOK_STATE_DELETED:
            return book_state_deleted()
