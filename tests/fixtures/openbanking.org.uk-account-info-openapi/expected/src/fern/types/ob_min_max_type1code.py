

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObMinMaxType1Code(str, enum.Enum):
    """
    Min Max type
    """

    FMMN = "FMMN"
    FMMX = "FMMX"

    def visit(self, fmmn: typing.Callable[[], T_Result], fmmx: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObMinMaxType1Code.FMMN:
            return fmmn()
        if self is ObMinMaxType1Code.FMMX:
            return fmmx()
