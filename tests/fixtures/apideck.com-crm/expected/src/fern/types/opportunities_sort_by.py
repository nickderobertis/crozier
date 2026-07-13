

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OpportunitiesSortBy(str, enum.Enum):
    """
    The field on which to sort the Opportunities
    """

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    TITLE = "title"
    WIN_PROBABILITY = "win_probability"
    MONETARY_AMOUNT = "monetary_amount"
    STATUS = "status"

    def visit(
        self,
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        win_probability: typing.Callable[[], T_Result],
        monetary_amount: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpportunitiesSortBy.CREATED_AT:
            return created_at()
        if self is OpportunitiesSortBy.UPDATED_AT:
            return updated_at()
        if self is OpportunitiesSortBy.TITLE:
            return title()
        if self is OpportunitiesSortBy.WIN_PROBABILITY:
            return win_probability()
        if self is OpportunitiesSortBy.MONETARY_AMOUNT:
            return monetary_amount()
        if self is OpportunitiesSortBy.STATUS:
            return status()
