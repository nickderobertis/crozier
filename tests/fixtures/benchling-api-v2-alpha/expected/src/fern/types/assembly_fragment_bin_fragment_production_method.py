

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblyFragmentBinFragmentProductionMethod(enum.StrEnum):
    EXISTING_CUT_SITES = "EXISTING_CUT_SITES"
    EXISTING_HOMOLOGY_REGIONS = "EXISTING_HOMOLOGY_REGIONS"
    PRIMER_PAIR = "PRIMER_PAIR"

    def visit(
        self,
        existing_cut_sites: typing.Callable[[], T_Result],
        existing_homology_regions: typing.Callable[[], T_Result],
        primer_pair: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssemblyFragmentBinFragmentProductionMethod.EXISTING_CUT_SITES:
            return existing_cut_sites()
        if self is AssemblyFragmentBinFragmentProductionMethod.EXISTING_HOMOLOGY_REGIONS:
            return existing_homology_regions()
        if self is AssemblyFragmentBinFragmentProductionMethod.PRIMER_PAIR:
            return primer_pair()
