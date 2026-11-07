

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VersionResponseCompatibilityPolicy(enum.StrEnum):
    BACKWARD_COMPATIBLE = "backward_compatible"
    BREAKING_CHANGES = "breaking_changes"

    def visit(
        self, backward_compatible: typing.Callable[[], T_Result], breaking_changes: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is VersionResponseCompatibilityPolicy.BACKWARD_COMPATIBLE:
            return backward_compatible()
        if self is VersionResponseCompatibilityPolicy.BREAKING_CHANGES:
            return breaking_changes()
