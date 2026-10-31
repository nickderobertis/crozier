

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSearchRequestFilterValue(enum.StrEnum):
    """
    The value of the property to filter the results by.  Possible values for object type include `page` or `data_source`.  **Limitation**: Currently the only filter allowed is `object` which will filter by type of object (either `page` or `data_source`)
    """

    PAGE = "page"
    DATA_SOURCE = "data_source"

    def visit(self, page: typing.Callable[[], T_Result], data_source: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSearchRequestFilterValue.PAGE:
            return page()
        if self is PostSearchRequestFilterValue.DATA_SOURCE:
            return data_source()
