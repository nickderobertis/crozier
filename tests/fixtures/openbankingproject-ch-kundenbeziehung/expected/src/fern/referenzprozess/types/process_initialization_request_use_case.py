

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessInitializationRequestUseCase(enum.StrEnum):
    """
    Spezifischer Use Case
    """

    KUNDENBEZIEHUNGSEROFFNUNG = "kundenbeziehungseroffnung"
    RE_IDENTIFICATION = "re_identification"
    AGE_VERIFICATION = "age_verification"
    EVV_LIFECYCLE = "evv_lifecycle"

    def visit(
        self,
        kundenbeziehungseroffnung: typing.Callable[[], T_Result],
        re_identification: typing.Callable[[], T_Result],
        age_verification: typing.Callable[[], T_Result],
        evv_lifecycle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessInitializationRequestUseCase.KUNDENBEZIEHUNGSEROFFNUNG:
            return kundenbeziehungseroffnung()
        if self is ProcessInitializationRequestUseCase.RE_IDENTIFICATION:
            return re_identification()
        if self is ProcessInitializationRequestUseCase.AGE_VERIFICATION:
            return age_verification()
        if self is ProcessInitializationRequestUseCase.EVV_LIFECYCLE:
            return evv_lifecycle()
