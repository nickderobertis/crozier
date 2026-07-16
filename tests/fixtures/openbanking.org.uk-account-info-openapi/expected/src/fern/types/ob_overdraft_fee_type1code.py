

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObOverdraftFeeType1Code(str, enum.Enum):
    """
    Overdraft fee type
    """

    FBAO = "FBAO"
    FBAR = "FBAR"
    FBEB = "FBEB"
    FBIT = "FBIT"
    FBOR = "FBOR"
    FBOS = "FBOS"
    FBSC = "FBSC"
    FBTO = "FBTO"
    FBUB = "FBUB"
    FBUT = "FBUT"
    FTOT = "FTOT"
    FTUT = "FTUT"

    def visit(
        self,
        fbao: typing.Callable[[], T_Result],
        fbar: typing.Callable[[], T_Result],
        fbeb: typing.Callable[[], T_Result],
        fbit: typing.Callable[[], T_Result],
        fbor: typing.Callable[[], T_Result],
        fbos: typing.Callable[[], T_Result],
        fbsc: typing.Callable[[], T_Result],
        fbto: typing.Callable[[], T_Result],
        fbub: typing.Callable[[], T_Result],
        fbut: typing.Callable[[], T_Result],
        ftot: typing.Callable[[], T_Result],
        ftut: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObOverdraftFeeType1Code.FBAO:
            return fbao()
        if self is ObOverdraftFeeType1Code.FBAR:
            return fbar()
        if self is ObOverdraftFeeType1Code.FBEB:
            return fbeb()
        if self is ObOverdraftFeeType1Code.FBIT:
            return fbit()
        if self is ObOverdraftFeeType1Code.FBOR:
            return fbor()
        if self is ObOverdraftFeeType1Code.FBOS:
            return fbos()
        if self is ObOverdraftFeeType1Code.FBSC:
            return fbsc()
        if self is ObOverdraftFeeType1Code.FBTO:
            return fbto()
        if self is ObOverdraftFeeType1Code.FBUB:
            return fbub()
        if self is ObOverdraftFeeType1Code.FBUT:
            return fbut()
        if self is ObOverdraftFeeType1Code.FTOT:
            return ftot()
        if self is ObOverdraftFeeType1Code.FTUT:
            return ftut()
