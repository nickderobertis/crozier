

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchemaDependencySubtypes(enum.StrEnum):
    AA_SEQUENCE = "aa_sequence"
    DNA_SEQUENCE = "dna_sequence"
    CUSTOM_ENTITY = "custom_entity"
    MIXTURE = "mixture"
    MOLECULE = "molecule"
    DNA_OLIGO = "dna_oligo"
    RNA_OLIGO = "rna_oligo"
    RNA_SEQUENCE = "rna_sequence"

    def visit(
        self,
        aa_sequence: typing.Callable[[], T_Result],
        dna_sequence: typing.Callable[[], T_Result],
        custom_entity: typing.Callable[[], T_Result],
        mixture: typing.Callable[[], T_Result],
        molecule: typing.Callable[[], T_Result],
        dna_oligo: typing.Callable[[], T_Result],
        rna_oligo: typing.Callable[[], T_Result],
        rna_sequence: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchemaDependencySubtypes.AA_SEQUENCE:
            return aa_sequence()
        if self is SchemaDependencySubtypes.DNA_SEQUENCE:
            return dna_sequence()
        if self is SchemaDependencySubtypes.CUSTOM_ENTITY:
            return custom_entity()
        if self is SchemaDependencySubtypes.MIXTURE:
            return mixture()
        if self is SchemaDependencySubtypes.MOLECULE:
            return molecule()
        if self is SchemaDependencySubtypes.DNA_OLIGO:
            return dna_oligo()
        if self is SchemaDependencySubtypes.RNA_OLIGO:
            return rna_oligo()
        if self is SchemaDependencySubtypes.RNA_SEQUENCE:
            return rna_sequence()
