

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RnaOligoNucleotideType(enum.StrEnum):
    """
    Nucleotide type of the Oligo.
    """

    DNA = "DNA"
    RNA = "RNA"

    def visit(self, dna: typing.Callable[[], T_Result], rna: typing.Callable[[], T_Result]) -> T_Result:
        if self is RnaOligoNucleotideType.DNA:
            return dna()
        if self is RnaOligoNucleotideType.RNA:
            return rna()
