

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogPluginCategory(enum.StrEnum):
    DISPLAY = "Display"
    AUTOMATION = "Automation"
    WORKFLOW = "Workflow"
    HARDWARE = "Hardware"

    def visit(
        self,
        display: typing.Callable[[], T_Result],
        automation: typing.Callable[[], T_Result],
        workflow: typing.Callable[[], T_Result],
        hardware: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogPluginCategory.DISPLAY:
            return display()
        if self is CatalogPluginCategory.AUTOMATION:
            return automation()
        if self is CatalogPluginCategory.WORKFLOW:
            return workflow()
        if self is CatalogPluginCategory.HARDWARE:
            return hardware()
