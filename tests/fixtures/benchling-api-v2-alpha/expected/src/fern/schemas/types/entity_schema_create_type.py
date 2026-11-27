

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EntitySchemaCreateType(enum.StrEnum):
    CUSTOM_ENTITY = "custom_entity"
    DNA_SEQUENCE = "dna_sequence"
    RNA_SEQUENCE = "rna_sequence"
    AA_SEQUENCE = "aa_sequence"
    MIXTURE = "mixture"
    DNA_OLIGO = "dna_oligo"
    RNA_OLIGO = "rna_oligo"
    MOLECULE = "molecule"
    ENTRY = "entry"

    def visit(
        self,
        custom_entity: typing.Callable[[], T_Result],
        dna_sequence: typing.Callable[[], T_Result],
        rna_sequence: typing.Callable[[], T_Result],
        aa_sequence: typing.Callable[[], T_Result],
        mixture: typing.Callable[[], T_Result],
        dna_oligo: typing.Callable[[], T_Result],
        rna_oligo: typing.Callable[[], T_Result],
        molecule: typing.Callable[[], T_Result],
        entry: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntitySchemaCreateType.CUSTOM_ENTITY:
            return custom_entity()
        if self is EntitySchemaCreateType.DNA_SEQUENCE:
            return dna_sequence()
        if self is EntitySchemaCreateType.RNA_SEQUENCE:
            return rna_sequence()
        if self is EntitySchemaCreateType.AA_SEQUENCE:
            return aa_sequence()
        if self is EntitySchemaCreateType.MIXTURE:
            return mixture()
        if self is EntitySchemaCreateType.DNA_OLIGO:
            return dna_oligo()
        if self is EntitySchemaCreateType.RNA_OLIGO:
            return rna_oligo()
        if self is EntitySchemaCreateType.MOLECULE:
            return molecule()
        if self is EntitySchemaCreateType.ENTRY:
            return entry()
