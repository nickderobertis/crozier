

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CardPrepaidType(str, enum.Enum):
    """
    Indicates a card's prepaid type, such as `NOT_PREPAID` or `PREPAID`.
    """

    UNKNOWN_PREPAID_TYPE = "UNKNOWN_PREPAID_TYPE"
    NOT_PREPAID = "NOT_PREPAID"
    PREPAID = "PREPAID"

    def visit(
        self,
        unknown_prepaid_type: typing.Callable[[], T_Result],
        not_prepaid: typing.Callable[[], T_Result],
        prepaid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardPrepaidType.UNKNOWN_PREPAID_TYPE:
            return unknown_prepaid_type()
        if self is CardPrepaidType.NOT_PREPAID:
            return not_prepaid()
        if self is CardPrepaidType.PREPAID:
            return prepaid()
