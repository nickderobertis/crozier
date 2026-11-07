

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TelInputStrategy(enum.StrEnum):
    LEGACY_SEQUENTIAL = "legacy_sequential"
    FORMATTED_SEQUENTIAL = "formatted_sequential"
    SEQUENTIAL_NATIONAL = "sequential_national"
    ATOMIC_NATIONAL = "atomic_national"
    ATOMIC_E164 = "atomic_e164"

    def visit(
        self,
        legacy_sequential: typing.Callable[[], T_Result],
        formatted_sequential: typing.Callable[[], T_Result],
        sequential_national: typing.Callable[[], T_Result],
        atomic_national: typing.Callable[[], T_Result],
        atomic_e164: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TelInputStrategy.LEGACY_SEQUENTIAL:
            return legacy_sequential()
        if self is TelInputStrategy.FORMATTED_SEQUENTIAL:
            return formatted_sequential()
        if self is TelInputStrategy.SEQUENTIAL_NATIONAL:
            return sequential_national()
        if self is TelInputStrategy.ATOMIC_NATIONAL:
            return atomic_national()
        if self is TelInputStrategy.ATOMIC_E164:
            return atomic_e164()
