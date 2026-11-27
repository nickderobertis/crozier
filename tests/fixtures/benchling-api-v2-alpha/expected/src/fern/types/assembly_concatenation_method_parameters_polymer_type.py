

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblyConcatenationMethodParametersPolymerType(enum.StrEnum):
    DNA = "DNA"
    RNA = "RNA"
    AA = "AA"

    def visit(
        self, dna: typing.Callable[[], T_Result], rna: typing.Callable[[], T_Result], aa: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AssemblyConcatenationMethodParametersPolymerType.DNA:
            return dna()
        if self is AssemblyConcatenationMethodParametersPolymerType.RNA:
            return rna()
        if self is AssemblyConcatenationMethodParametersPolymerType.AA:
            return aa()
