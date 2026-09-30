

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchByIdentifierRequestRepresentation(enum.StrEnum):
    ALL = "all"
    SMILES = "smiles"
    REACH = "reach"
    STDINCHI = "stdinchi"
    STDINCHIKEY = "stdinchikey"
    NAMES = "names"
    IUPAC_NAME = "iupac_name"
    SYNONYM = "synonym"
    CAS = "cas"
    EINECS = "einecs"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        smiles: typing.Callable[[], T_Result],
        reach: typing.Callable[[], T_Result],
        stdinchi: typing.Callable[[], T_Result],
        stdinchikey: typing.Callable[[], T_Result],
        names: typing.Callable[[], T_Result],
        iupac_name: typing.Callable[[], T_Result],
        synonym: typing.Callable[[], T_Result],
        cas: typing.Callable[[], T_Result],
        einecs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchByIdentifierRequestRepresentation.ALL:
            return all_()
        if self is SearchByIdentifierRequestRepresentation.SMILES:
            return smiles()
        if self is SearchByIdentifierRequestRepresentation.REACH:
            return reach()
        if self is SearchByIdentifierRequestRepresentation.STDINCHI:
            return stdinchi()
        if self is SearchByIdentifierRequestRepresentation.STDINCHIKEY:
            return stdinchikey()
        if self is SearchByIdentifierRequestRepresentation.NAMES:
            return names()
        if self is SearchByIdentifierRequestRepresentation.IUPAC_NAME:
            return iupac_name()
        if self is SearchByIdentifierRequestRepresentation.SYNONYM:
            return synonym()
        if self is SearchByIdentifierRequestRepresentation.CAS:
            return cas()
        if self is SearchByIdentifierRequestRepresentation.EINECS:
            return einecs()
