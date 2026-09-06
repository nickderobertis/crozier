

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DealerDbModelsLicenseLicenseActivationType(enum.StrEnum):
    """
    The type of license (e.g. EDT, EDT Lite)
    """

    EDT = "EDT"
    EDT_LITE = "EDTLite"

    def visit(self, edt: typing.Callable[[], T_Result], edt_lite: typing.Callable[[], T_Result]) -> T_Result:
        if self is DealerDbModelsLicenseLicenseActivationType.EDT:
            return edt()
        if self is DealerDbModelsLicenseLicenseActivationType.EDT_LITE:
            return edt_lite()
