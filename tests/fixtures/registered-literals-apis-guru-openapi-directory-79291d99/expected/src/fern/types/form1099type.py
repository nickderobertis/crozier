

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Form1099Type(enum.StrEnum):
    """
    Form 1099 Type
    """

    FORM1099TYPE_UNKNOWN = "FORM_1099_TYPE_UNKNOWN"
    FORM1099TYPE_MISC = "FORM_1099_TYPE_MISC"
    FORM1099TYPE_K = "FORM_1099_TYPE_K"

    def visit(
        self,
        form1099type_unknown: typing.Callable[[], T_Result],
        form1099type_misc: typing.Callable[[], T_Result],
        form1099type_k: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Form1099Type.FORM1099TYPE_UNKNOWN:
            return form1099type_unknown()
        if self is Form1099Type.FORM1099TYPE_MISC:
            return form1099type_misc()
        if self is Form1099Type.FORM1099TYPE_K:
            return form1099type_k()
