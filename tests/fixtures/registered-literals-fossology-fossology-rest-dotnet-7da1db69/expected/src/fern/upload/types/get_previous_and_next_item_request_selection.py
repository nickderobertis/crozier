

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPreviousAndNextItemRequestSelection(enum.StrEnum):
    WITH_LICENSES = "withLicenses"
    NO_CLEARING = "noClearing"

    def visit(
        self, with_licenses: typing.Callable[[], T_Result], no_clearing: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetPreviousAndNextItemRequestSelection.WITH_LICENSES:
            return with_licenses()
        if self is GetPreviousAndNextItemRequestSelection.NO_CLEARING:
            return no_clearing()
