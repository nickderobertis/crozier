

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchFiltersExecutionDomainsItem(enum.StrEnum):
    HUMAN = "HUMAN"
    DIGITAL = "DIGITAL"
    PHYSICAL = "PHYSICAL"

    def visit(
        self,
        human: typing.Callable[[], T_Result],
        digital: typing.Callable[[], T_Result],
        physical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchFiltersExecutionDomainsItem.HUMAN:
            return human()
        if self is SearchFiltersExecutionDomainsItem.DIGITAL:
            return digital()
        if self is SearchFiltersExecutionDomainsItem.PHYSICAL:
            return physical()
