

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblyHomologyMethodParametersAmbiguousConstructPreference(enum.StrEnum):
    USE_LARGER_FRAGMENT_IN_FIRST_BIN = "USE_LARGER_FRAGMENT_IN_FIRST_BIN"
    USE_SMALER_FRAGMENT_IN_FIRST_BIN = "USE_SMALER_FRAGMENT_IN_FIRST_BIN"

    def visit(
        self,
        use_larger_fragment_in_first_bin: typing.Callable[[], T_Result],
        use_smaler_fragment_in_first_bin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssemblyHomologyMethodParametersAmbiguousConstructPreference.USE_LARGER_FRAGMENT_IN_FIRST_BIN:
            return use_larger_fragment_in_first_bin()
        if self is AssemblyHomologyMethodParametersAmbiguousConstructPreference.USE_SMALER_FRAGMENT_IN_FIRST_BIN:
            return use_smaler_fragment_in_first_bin()
