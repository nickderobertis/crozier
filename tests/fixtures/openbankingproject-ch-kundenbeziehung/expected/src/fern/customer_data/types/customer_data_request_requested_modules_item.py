

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerDataRequestRequestedModulesItem(enum.StrEnum):
    BASISDATEN_MODULE = "basisdaten_module"
    ERWEITERTE_DATEN_MODULE = "erweiterte_daten_module"
    IDENTIFIKATION_MODULE = "identifikation_module"
    BACKGROUND_CHECKS_MODULE = "background_checks_module"

    def visit(
        self,
        basisdaten_module: typing.Callable[[], T_Result],
        erweiterte_daten_module: typing.Callable[[], T_Result],
        identifikation_module: typing.Callable[[], T_Result],
        background_checks_module: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomerDataRequestRequestedModulesItem.BASISDATEN_MODULE:
            return basisdaten_module()
        if self is CustomerDataRequestRequestedModulesItem.ERWEITERTE_DATEN_MODULE:
            return erweiterte_daten_module()
        if self is CustomerDataRequestRequestedModulesItem.IDENTIFIKATION_MODULE:
            return identifikation_module()
        if self is CustomerDataRequestRequestedModulesItem.BACKGROUND_CHECKS_MODULE:
            return background_checks_module()
