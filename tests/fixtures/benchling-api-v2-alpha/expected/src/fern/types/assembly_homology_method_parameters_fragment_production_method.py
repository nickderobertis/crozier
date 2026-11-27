

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblyHomologyMethodParametersFragmentProductionMethod(enum.StrEnum):
    EXISTING_HOMOLOGY_REGIONS = "EXISTING_HOMOLOGY_REGIONS"

    def visit(self, existing_homology_regions: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssemblyHomologyMethodParametersFragmentProductionMethod.EXISTING_HOMOLOGY_REGIONS:
            return existing_homology_regions()
